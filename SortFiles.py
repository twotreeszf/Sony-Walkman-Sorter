#coding: utf-8
import sys
import os
from os import path

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
    sortKey = tagName + 'SORT'

    tagSort = meta.get(sortKey)
    if tagSort and len(tagSort) and tagSort[0] != '':
        tagSort = tagSort[0]
        if not beginWithCJK(tagSort):
            return False

    tag = meta.get(tagName)
    if (not tag) or (not len(tag)) or (tag[0] == ''):
        return False
    else:
        tag = tag[0]
        if not beginWithCJK(tag):
            return False
        else:
            firstLetters = CJKFirstLetters(tag)
            meta[sortKey] = firstLetters
            print('[info] {0}: processed [{1}] is \"{2}\"'.format(path, sortKey, firstLetters))
            return True

def setSortTags(path):
    ext = os.path.splitext(path)[1]
    meta = None

    try:
        if ext == '.mp3':
            meta = MP3(path)
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