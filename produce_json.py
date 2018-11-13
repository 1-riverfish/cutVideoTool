#!/usr/bin/python3
# -*- coding:utf-8 -*-
# python3 object to json object
# video_id = groupid_start
# youdaoyun api from zh to en

import json
import re
import copy
import time
import datetime
import hashlib
import requests
import sys

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

# 生成md5SIGN
def tmd5(zh):
    #创建md5对象
    hl=hashlib.md5()
    mix=APPID+zh+SALT+APPKEY
    print("mix "+mix)
    hl.update(mix.encode(encoding='utf-8'))
    return (hl.hexdigest()).upper()

# 请求API 获取对应翻译
def ten(zh):
    SIGN=tmd5(zh)
    getUrl=URL+"?"+"q="+zh+"&from="+FROM+"&to="+TO+"&appKey="+APPID+"&salt="+SALT+"&sign="+SIGN

    # 发送请求
    request = requests.session()
    response = request.get(getUrl,headers=header_dict)
    return response.text

# 命名 规则
# 小组编号 和 视频开始编号
GROUPID = int(sys.argv[1])
START = int(sys.argv[2])

#有道云翻译API
URL="http://openapi.youdao.com/api"
FROM="zh_CHS"
TO="EN"
APPID="7917fa6b0afb4b56"
APPKEY="NN2kirWKzfavjFnOHZnn0suaMHbC5wS4"
SALT="2"
header_dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

# 时间信息
TODAY = str(datetime.date.today())
NOW = str(time.strftime("%H:%M:%S"))

# 基本json格式 
pjson_info_zh = {
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

pjson_info_en = {
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

pjson_sentence_zh = {
    "caption": "短视频的中文描述",
    "video_id": "video_id",
    "sen_id": 0
}

pjson_sentence_en = {
    "caption": "Description of the video in english",
    "video_id": "video_id",
    "sen_id": 0
}

# 获取pjson_info对象中的videos和sentences
videosList_zh = pjson_info_zh["videos"]
sentencesList_zh = pjson_info_zh["sentences"]

videosList_en = pjson_info_en["videos"]
sentencesList_en = pjson_info_en["sentences"]

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
    pjson_video["end time"]=end_time
    pjson_video["video_id"]="video"+str(GROUPID)+"_"+str(i+START)
    pjson_video["id"]=int(i)

    # 构造pjson_sentence对象
    pjson_sentence_zh["caption"]=caption
    pjson_sentence_zh["video_id"]="video"+str(GROUPID)+"_"+str(i+START)
    pjson_sentence_zh["sen_id"]=int(i)
    
    pjson_sentence_en["caption"]=json.loads(ten(caption))["translation"][0]
    pjson_sentence_en["video_id"]="video"+str(GROUPID)+"_"+str(i+START)
    pjson_sentence_en["sen_id"]=int(i)
    
    # 添加pjson_video 和　pjson_sentence 对象到　pjson_info对应的列表
    videosList_zh.append(copy.deepcopy(pjson_video))
    sentencesList_zh.append(copy.deepcopy(pjson_sentence_zh))
    videosList_en.append(copy.deepcopy(pjson_video))
    sentencesList_en.append(copy.deepcopy(pjson_sentence_en))
   
    i=i+1
    line = f.readline()
f.close()

# python对象　--> json字符串
json_str_zh=json.dumps(pjson_info_zh,ensure_ascii=False)
json_str_en=json.dumps(pjson_info_en,ensure_ascii=False)
# 将字符串写入文件
save_to_file("zh.json", json_str_zh)
save_to_file("en.json", json_str_en)

