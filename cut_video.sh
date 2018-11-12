#!/bin/bash
# Deep-learning homework tools cut videos fragment

IFS=$'\n'
SOURCE_VIDEO_NAME="source.mp4"
GROUPID=1
PERSONID=0

#用户输入基本信息
echo "输出文件命名规则"
read -p "请输入小组编号: " GROUPID
read -p "请输入待处理视频开始编号: " PERSONID

# 判断是否存在output文件夹
if [ -d output ]
then
    echo "output dir exists!"
    rm -rf ./output/*
else
    mkdir output
fi

# 判断是否存在source.mp4文件
if [ -f source.mp4 ]
then
    echo " source.mp4 file exists!"
else
    echo " source.mp4 file doesn't exist! Please move to current directory."
    exit
fi


echo "开始切割..."
# i为待处理视频在组内视频开始编号
i=0
i=$[$i+$PERSONID]
for entry in $(cat ./time.txt)
do
    # 从文件读取开始时间和视频时长
    START=`echo $entry | cut -d"~" -f1`
    TIME=`echo $entry | cut -d"~" -f2`
    echo "start-time:$START  time:$TIME"

    # 提取原始视频片段
    OUTPUTNAME="${GROUPID}_$i"
    echo $OUTPUTNAME
    ffmpeg -i "$SOURCE_VIDEO_NAME" -ss $START -t $TIME -c:v copy -c:a copy "./output/$OUTPUTNAME.mp4"

    # 从视频中分离音频
    ffmpeg -i "./output/$OUTPUTNAME.mp4" -vn -y -ar 44100 -acodec copy  "./output/$OUTPUTNAME.aac"

    i=$[$i+1]
done

i=$[ $i-$PERSONID ]

# 执行python脚本　分离手语和视频
cp capture_video.py ./output
cd output
# 传入所在行参数
python3 capture_video.py $i $GROUPID $PERSONID

# 删除*.mp4
rm -f *.mp4
rm -f capture_video.py
cd ..
echo "Done."
