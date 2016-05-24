#coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from os import path

from mutagen.easyid3 import EasyID3
EasyID3.RegisterTextKey('ALBUMARTIST', 'TPE2')
EasyID3.RegisterTextKey('ALBUMARTISTSORT', 'TSO2')

from mutagen.mp3 import EasyMP3 as MP3
from mutagen.easymp4 import EasyMP4 as MP4
from pypinyin import lazy_pinyin

def beginWithCJK(str):
    if u'\u4e00' <= str[0] <= u'\u9fff':
        return True
    else:
        return False

def CJKFirstLetters(str):
    pinyins = lazy_pinyin(str)
    firstLetters = ''
    for pinyin in pinyins:
        firstLetters += pinyin[0]

    return firstLetters

def checkTagMakeSort(path, meta, tagName):
    value = meta.get(tagName)
    if value and len(value) and value[0] != '':
        value = value[0]
        if not beginWithCJK(value):
            return False
        else:
            firstLetters = CJKFirstLetters(value).upper()
            newValue = firstLetters[0:3] + '^' + value
            meta[tagName] = newValue
            print('[info] {0}: processed [{1}] is \"{2}\"'.format(path, tagName, newValue))
            return True

    return False

def setSortTags(path):
    ext = os.path.splitext(path)[1].lower()
    meta = None

    try:
        if ext == '.mp3':
            meta = MP3(path)
            meta.tags
        elif ext == '.m4a':
            meta = MP4(path)
        else:
            return
    except:
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
        except:
            pass

def processFilesInFolder(folder):
    dirlist = os.listdir(folder)
    for x in dirlist:
        abspath = path.join(folder, x)
        if(path.isfile(abspath)):
            setSortTags(abspath)
        elif (path.isdir(abspath)):
            processFilesInFolder(abspath)

if __name__ == '__main__':
    if len(sys.argv) < 2 :
        print('[error] need param: target folder path')
    else:
        folder = sys.argv[1]
        if not path.isdir(folder):
            print('[error] target folder not exist')
        else:
            processFilesInFolder(folder)