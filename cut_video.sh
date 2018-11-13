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
for entry in $(cat ./info.txt)
do
    # 从文件读取开始时间和视频时长
    START=`echo $entry | cut -d" " -f1`
    END=`echo $entry | cut -d" " -f2`

    SH=`echo $START | cut -d":" -f1`
    SS=`echo $START | cut -d":" -f2`
    EH=`echo $END | cut -d":" -f1`
    ES=`echo $END | cut -d":" -f2`
    TIME=$[ $EH*60+$ES-$SH*60-$SS ]
    echo "start-time:$START  end-time:$END  time:$TIME"
    # 判断视频时长是否正确
    if [ $TIME -le 0 ]
    then
        echo "ERROR::视频时长小于0"
        exit
    fi

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
cp produce_json.py ./output
cp info.txt ./output
cd output
# 传入所在行参数
python3 capture_video.py $i $GROUPID $PERSONID
python3 produce_json.py $GROUPID $PERSONID
# 删除*.mp4
rm -f *.mp4
rm -f capture_video.py produce_json.py info.txt
cd ..
echo "Done."
