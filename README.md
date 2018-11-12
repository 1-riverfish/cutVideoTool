# 切割视频工具

深度学习作业**批量**切割视频

## 运行环境

- Linux
  - ffmpeg
  - python3

## 使用

1. 克隆仓库、安装依赖项

```bash
$ git clone https://github.com/1-riverfish/cut_video.git
$ cd cut_video
$ sudo chmod a+x cut_video.sh capture_video.mp4
$ mv /path/to/sourcevideo ./source.mp4　# 将待切割视频移动到Cut_video目录下并更名为source.mp4
$ sudo apt update && sudo apt upgrade
$ sudo apt install ffmpeg python3

```

1. 修改time.txt文件

\*\*:\*\*~--:--
\*\*:\*\*为**片段开始时间**　--:--为**片段持续时长**
e.g:

```
38:20~00:22
40:14~00:16
40:42~00:14
41:29~00:14
41:56~00:10
42:07~00:17
43:17~00:28
45:40~00:16
46:48~00:26
48:20~00:30

```

1. 执行脚本

```bash
$ ./cut_video.sh

```

output文件夹即为输出目录

## 修改

可修改cut_video.sh capture_video.py文件中的变量以**更改输出视频、音频的命名规则**

