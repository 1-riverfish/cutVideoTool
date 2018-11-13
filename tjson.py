#!/usr/bin/python3
# -*- coding:utf-8 -*-
# python3 object to json object
# video_id = groupid_start

import json
import re
import copy
import time
import datetime

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

# 命名 规则
# 小组编号 和 视频开始编号
GROUPID = 1
START = 0

# 时间信息
TODAY = str(datetime.date.today())
NOW = str(time.strftime("%H:%M:%S"))

# 基本json格式 
pjson_info = {
    "info": {
        "contributor": "Group"+str(GROUPID),
        "data_created": TODAY+" "+NOW,
        "version": "1.0",
        "description": "Deep-learning course homework.",
        "year": "2018"
    },
    "videos": [],
    "sentences": []
}
pjson_video = {
    "category": 0,
    "url": "http://www.github.com",
    "video_id": "video_id",
    "start time": "00:00",
    "end time": "10:00",
    "split": "train",
    "id": 0
}
pjson_sentence = {
    "caption": "短视频的中文描述",
    "video_id": "video_id",
    "sen_id": 0
}

# 获取pjson_info对象中的videos和sentences
videosList = pjson_info["videos"]
sentencesList = pjson_info["sentences"]

i=0
# 读取文件内容
f = open("info.txt")
line = f.readline()
while line:
    linelist = re.split(r"[ ]",line)

    start_time = linelist[0]
    end_time = linelist[1]
    category = linelist[2]
    url = linelist[3].strip("\"")
    caption=linelist[4].strip("\n").strip("\"")

    # 构造pjson_video对象
    pjson_video["category"] = int(category)
    pjson_video["url"] = url
    pjson_video["start time"]=start_time
    pjson_video["end_time"]=end_time
    pjson_video["video_id"]="video"+str(GROUPID)+"_"+str(i+START)
    pjson_video["id"]=int(i)

    # 构造pjson_sentence对象
    pjson_sentence["caption"]=caption
    pjson_sentence["video_id"]="video"+str(GROUPID)+"_"+str(i+START)
    pjson_sentence["sen_id"]=int(i)
    
    # 添加pjson_video 和　pjson_sentence 对象到　pjson_info对应的列表
    videosList.append(copy.deepcopy(pjson_video))
    sentencesList.append(copy.deepcopy(pjson_sentence))
   
    i=i+1
    line = f.readline()
f.close()

# python对象　--> json字符串
json_str=json.dumps(pjson_info,ensure_ascii=False)
# 将字符串写入文件
save_to_file("zh.json", json_str)


    

