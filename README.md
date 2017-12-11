# Sony-Walkman-Sorter
Change log:

添加了日文支持。以各个歌曲罗马音首字母进行排序。


## 背景
### Sony Walkman NW-A15/25 NW-ZX1/2/100、iBasso DX50/80/90 等HiFi播放器不能按照中文歌手、专辑、歌名进行排序显示，中文都被归到了etc下，导致查找中文歌曲和歌手非常麻烦
### 我综合了以下资料，搞定了这个问题，经测试可实现中文歌曲按照歌手、专辑、歌名准确排序，而且中文信息前并不会出现可见字母前缀！
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

## 使用方法
1. build目录下有打包好的处理工具。对应的操作系统下有SortFilesiBasso和SortFilesSony两个排序工具，
SortFilesiBasso用于DX50/80/90/100等不支持sort tags的机型，排序后歌名、歌手、专辑名称前面会出现字母前缀
SortFilesSony用于ZX1/2/100 A15/25等支持支持sort tags的机型，排序后不会出现字母前缀
2. 将对应的工具拷贝到音乐文件所在目录，直接双击或者在命令行之行即可。会自动跳过已处理过的和英文歌曲，所以下次增加了音频只需要再运行一次即可。Windows用户需要先安装vcredist_x86.exe

作者:twotrees
Email:twotrees.zf@gmail.com
QQ:329292657

![](/1.jpg)
![](/2.jpg)
![](/3.jpg)

