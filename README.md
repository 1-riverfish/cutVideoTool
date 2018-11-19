# 深度学习作业小工具

深度学习作业**批量**切割视频

- 自动从源视频中切割出**hand.avi**、**video.api**及**音频**
- 自动生成符合格式要求的**en.json**及**zh.json**
- 自动生成的文件均**满足命名规则**
- 当前版本**一次只能处理一期视频**

## 运行环境

- Linux(没有安装Linux操作系统的同学可以把**格式符合要求的txt文件**和**源视频**发给我，**只需要中文版本**)
  - ffmpeg
  - python3
  - pip3 install opencv-python
- **联网**(调用有道云API实现自动翻译)

## 使用

1. 克隆仓库、安装依赖项

```bash
$ git clone https://github.com/1-riverfish/cut_video.git
$ cd cut_video
$ sudo chmod a+x cut_video.sh capture_video.py produce_json.py
$ # 将待切割视频移动到cut_video目录下并更名为source.mp4
$ sudo apt update && sudo apt upgrade
$ sudo apt install ffmpeg python3

```

2. 修改info.txt文件
   info.txt文件是示例文件，在观看完视频后记录片段开始时间、结束时间并判定类别.其中，

   第一项为片段开始时间(片段在source.mp4中的开始时间)

   第二项为片段结束时间(片段在source.mp4中的结束时间)

   第三项为片段类别

   第四项为source.mp4的网址

   第五项为你对该片段的中文描述

> 注意格式要求　切换到英文输入法，每一项之间用**英文输入法的空格**隔开

```
40:14 40:26 1 "http://tv.cctv.com/2018/11/05/VIDEOLwTQVX7na66SDwmd6tE181105.shtml" "警察正在调查一处民宅"
40:42 40:56 2 "http://tv.cctv.com/2018/11/05/VIDEOLwTQVX7na66SDwmd6tE181105.shtml" "人们在路上示威游行"
41:29 41:43 4 "http://tv.cctv.com/2018/11/05/VIDEOLwTQVX7na66SDwmd6tE181105.shtml" "人们在街上行走"
41:56 42:06 4 "http://tv.cctv.com/2018/11/05/VIDEOLwTQVX7na66SDwmd6tE181105.shtml" "一个男人正在接受采访"

```

3. 执行脚本

```bash
$ ./cut_video.sh

```

> 此处会提示输入小组编号及组内视频标号，例如我所在的小组为第四组，则小组编号为4,我们组需要完成50个训练集，我负责其中40~49,则组内视频编号为40

**output文件夹即为输出目录**

最终成果

![](http://39.105.38.48/images/2018/11/13/_002.png)

## 修改

可修改cut_video.sh capture_video.py produce.py文件中的变量以**更改输出视频、音频的命名规则**

> Any question please contact QQ:1020072294

