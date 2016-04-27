# Sony-Walkman-Sorter
## 背景
### Sony Walkman NW-A15/25 NW-ZX1/2/100 乃我广大Sony大法死忠粉簇拥之神器也
### 满满的童年回忆＋最新黑科技回放加持有木有 然大法Walkman不能按照中文歌手、专辑、歌名进行排序显示，中文的一切都被归到了万恶的etc下
### 这无疑是一个大悲剧，也是一个噩耗 那么多的中文歌找起来太麻烦了 枉费了ZX100那128GB的海量存储 回归音乐本质的路上充满了坎坷啊……
### 于是网上各路大神有招的出招有力的出力，都没有的出口水以及严重围观，然效果依然差强人意
### 直到小弟我综合了以下所有资料，集各家之大成，终于搞定了这个问题，经测试可实现中文歌曲按照歌手、专辑、歌名准确排序，而且中文信息前并不会出现可见字母前缀！在此对各路大神、各路开源方案表示感谢：
- [walkman 自动添加中文排序信息的脚本](http://tieba.baidu.com/p/3436217262)
- [SONY Walkman NWZ-A17 不專業的開箱文](http://blog.xuite.net/terry30173/2dx/275537359-SONY+Walkman+NWZ-A17+%E4%B8%8D%E5%B0%88%E6%A5%AD%E7%9A%84%E9%96%8B%E7%AE%B1%E6%96%87)
- [Walkman-sort-by-title](https://github.com/agmcs/Walkman-sort-by-title/blob/master/TitleSort2.0.py)
- [https://mutagen.readthedocs.org/en/latest/man/index.html]()
- [http://mutagen.readthedocs.org/en/latest/api/mp4.html]()
- [Tag field mappings](http://help.mp3tag.de/main_tags.html)

## 支持系统
理论上支持Windows／Mac／Linux系统，只要有Python即可，个人仅在Mac上测试
## 支持机型
理论上支持所有非智能Walkman，个人仅在ZX100上测试

## 使用方法(技术汪请略过)
- 安装Git [https://git-scm.com/downloads]()
- 安装Python [https://www.python.org/downloads/]()
- 安装pip [https://pip.pypa.io/en/stable/installing/]()
- 配置环境：（Windows下打开Git提供的命令行）

```
cd ~/Documents
git checkout git@github.com:twotreeszf/Sony-Walkman-Sorter.git
cd Sony-Walkman-Sorter
pip install -r requirements.txt
```
- 将需要处理的音乐文件到同一个目录[xxx]下，输入命令批量转换[xxx]下的所有文件（目前支持.mp3, .m4a）例如：
 
```
python SortFiles.py ~/Documents/musics

```
- 然后拷回Walkman，搞定！

![](/1.jpg)
![](/2.jpg)
![](/3.jpg)

