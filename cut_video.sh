#!/bin/bash
# Deep-learning homework tools cut videos fragment

IFS=$'\n'
SOURCE_VIDEO_NAME="source.mp4"
GROUPID=1
PERSONID=0

# 判断是否存在output文件夹
if [ -d output ]
then
    echo "output dir exists!"
    rm -rf ./output/*
else
    mkdir output
fi

echo "Cutting..."
i=0
for entry in $(cat ./time.txt)
do
    # 从文件读取开始时间和视频时长
    START=`echo $entry | cut -d"~" -f1`
    TIME=`echo $entry | cut -d"~" -f2`
    echo "start-time:$START  time:$TIME"

    # 提取原始视频片段
    # OUTPUTNAME="${GROUPID}_$PERSONID$i"
    OUTPUTNAME=$i
    ffmpeg -i "$SOURCE_VIDEO_NAME" -ss $START -t $TIME -c:v copy -c:a copy "./output/$OUTPUTNAME.mp4"

    # 从视频中分离音频
    ffmpeg -i "./output/$OUTPUTNAME.mp4" -vn -y -ar 44100 -acodec copy  "./output/$OUTPUTNAME.aac"

    i=$[$i+1]
done

# 执行python脚本　分离手语和视频
cp capture_video.py ./output
cd output
./capture_video.py

# 删除*.mp4
rm -f *.mp4
rm -f capture_video.py
cd ..
echo "Done."
