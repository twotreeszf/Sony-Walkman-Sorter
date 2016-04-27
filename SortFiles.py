#coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from os import path

from mutagen.mp3 import EasyMP3 as MP3
from mutagen.easymp4 import EasyMP4 as MP4

def chineseCharacterLetter(str):
    if str > u'\u9fa5' or str < u'\u4e00':
        return None
    str = str.encode('gbk', 'ignore')
    asc = ord(str[0]) * 256 + ord(str[1]) - 65536
    if asc >= -20319 and asc <= -20284: 
        return 'a' 
    if asc >= -20283 and asc <= -19776: 
        return 'b' 
    if asc >= -19775 and asc <= -19219: 
        return 'c' 
    if asc >= -19218 and asc <= -18711: 
        return 'd' 
    if asc >= -18710 and asc <= -18527: 
        return 'e' 
    if asc >= -18526 and asc <= -18240: 
        return 'f' 
    if asc >= -18239 and asc <= -17923: 
        return 'g' 
    if asc >= -17922 and asc <= -17418: 
        return 'h' 
    if asc >= -17417 and asc <= -16475: 
        return 'j' 
    if asc >= -16474 and asc <= -16213: 
        return 'k' 
    if asc >= -16212 and asc <= -15641: 
        return 'l' 
    if asc >= -15640 and asc <= -15166: 
        return 'm' 
    if asc >= -15165 and asc <= -14923: 
        return 'n' 
    if asc >= -14922 and asc <= -14915: 
        return 'o' 
    if asc >= -14914 and asc <= -14631: 
        return 'p' 
    if asc >= -14630 and asc <= -14150: 
        return 'q' 
    if asc >= -14149 and asc <= -14091: 
        return 'r' 
    if asc >= -14090 and asc <= -13119: 
        return 's' 
    if asc >= -13118 and asc <= -12839: 
        return 't' 
    if asc >= -12838 and asc <= -12557: 
        return 'w' 
    if asc >= -12556 and asc <= -11848: 
        return 'x' 
    if asc >= -11847 and asc <= -11056: 
        return 'y' 
    if asc >= -11055 and asc <= -10247: 
        return 'z'
    else:
        return None

def checkTagMakeSort(path, meta, tagName):
    tag = meta.get(tagName)
    if (not tag) or (not len(tag)) or (tag[0] == ''):
        print('[warning] dont have [{0}] info'.format(tagName))
    else:
        tag = tag[0]
        letter = chineseCharacterLetter(tag)
        if not letter:
            print('[info] {0}: [{1}] is \"{2}\", not chinese'.format(path, tagName, tag))
        else:
            tagSortName = tagName + 'SORT'
            tagSort = letter + tag
            meta[tagSortName] = tagSort
            print('[info] {0}: processed [{1}] is \"{2}\"'.format(path, tagSortName, tagSort))

def setSortTags(path):
    ext = os.path.splitext(path)[1]
    meta = None

    try:
        if ext == '.mp3':
            meta = MP3(path)
        elif ext == '.m4a':
            meta = MP4(path)
        else:
            print('[info] {0} not audio file'.format(path))
            return
    except:
        pass

    if meta:
        try:
            checkTagMakeSort(path, meta, 'ALBUM')
            checkTagMakeSort(path, meta, 'ALBUMARTIST')
            checkTagMakeSort(path, meta, 'ARTIST')
            checkTagMakeSort(path, meta, 'TITLE')

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