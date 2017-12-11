#!/usr/bin/python3
# -*- coding:utf-8 -*-
import sys

import os
from os import path
import logging
import JKConverter

logging.basicConfig(level=logging.DEBUG)

from mutagen.easyid3 import EasyID3
EasyID3.RegisterTextKey('ALBUMARTIST', 'TPE2')
EasyID3.RegisterTextKey('ALBUMARTISTSORT', 'TSO2')

from mutagen.mp3 import EasyMP3 as MP3
from mutagen.easymp4 import EasyMP4 as MP4
from mutagen.flac import FLAC

from pypinyin import lazy_pinyin, Style

def beginWithCJK(str):
    if u'\u2e80' <= str[0] <= u'\u9fff':
        return True
    else:
        return False

def CJKFirstLetters(str):
    pinyins = lazy_pinyin(str, style=Style.FIRST_LETTER, errors=returnJapaneseKoreanPinyin)
    firstLetters = ''
    for pinyin in pinyins:
        firstLetters += pinyin

    return firstLetters

def checkTagMakeSort(path, meta, tagName):
    sortKey = tagName + 'SORT'

    tagSort = meta.get(sortKey)
    if tagSort and len(tagSort) and tagSort[0] != '':
        tagSort = tagSort[0]
        if not beginWithCJK(tagSort):
            logging.debug('Not processing tag {0} because its non-CJK'.format(tagSort))
            return False

    tag = meta.get(tagName)
    if (not tag) or (not len(tag)) or (tag[0] == ''):
        logging.debug('Not processing tag {0} because its tag is invalid or empty'.format(tag))
        return False
    else:
        tag = tag[0]
        if not beginWithCJK(tag):
            logging.debug('Not processing tag {0} because its non-CJK'.format(tag))
            return False
        else:
            firstLetters = CJKFirstLetters(tag)
            meta[sortKey] = firstLetters
            logging.info('{0}: processed [{1}] is \"{2}\", formally \"{3}\"'.format(path, sortKey, firstLetters, tag))
            return True

def setSortTags(path):
    ext = os.path.splitext(path)[1].lower()
    meta = None

    try:
        if ext == '.mp3':
            meta = MP3(path)
        elif ext == '.m4a':
            meta = MP4(path)
        elif ext == '.flac':
            meta = FLAC(path)
        else:
            return
    except:
        logging.warning('unknown file type:{0}'.format(path))
        pass

    if meta:
        tagsToProcess = ('ALBUM', 'ALBUMARTIST', 'ARTIST', 'TITLE')
        save = False
        try:
            for tag in tagsToProcess:
                processed = checkTagMakeSort(path, meta, tag)
                if (processed):
                    save = True
            if save:
                meta.save()
        except Exception as e:
            logging.warning('Save tag for {0} failure'.format(path))
            logging.exception(e)
            pass

def processFilesInFolder(folder):
    logging.info('processing folder [{0}]'.format(folder))
    dirlist = os.listdir(folder)
    for x in dirlist:
        abspath = path.join(folder, x)
        if(path.isfile(abspath)):
            setSortTags(abspath)
        elif (path.isdir(abspath)):
            processFilesInFolder(abspath)


def isEngAndNum(aChar):
    if aChar == ' ':
        return True
    if aChar < '0':
        return False
    if aChar <= '9':
        return True
    if aChar < 'A':
        return False
    if aChar <= 'Z':
        return True
    if aChar < 'a':
        return False
    if aChar <= 'z':
        return True
    return False


def returnJapaneseKoreanPinyin(unknownStr):
    returnedStr = JKConverter.convert(unknownStr)
    pinyin = ""
    for returnedChar in returnedStr:
        if isEngAndNum(returnedChar):
            pinyin += returnedChar
    return pinyin

if __name__ == '__main__':
    message = '''
    Walkman file sorter by twotrees, Email:twotrees.zf@gmail.com, QQ:329292657

    Usage:

    Process in current folder:
    ./SortFiles

    Process in specified folder:
    ./SortFiles [folder_path]

    '''
    print(message)

    folder = None
    if len(sys.argv) < 2 :
        logging.info('No folder path specified, will process current folder')
        folder = folder = os.getcwd()
    else:
        folder = sys.argv[1]
        if not path.isdir(folder):
            logging.error('Target folder does not exist')
            folder = None

    if folder:
        processFilesInFolder(folder)
