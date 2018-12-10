#!/usr/bin/python3
import json
import requests
import re
import hashlib
import sys
import copy

def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

# 生成md5SIGN
def tmd5(zh):
    #创建md5对象
    hl=hashlib.md5()
    mix=APPID+zh+SALT+APPKEY
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

# 有道云翻译API
URL="http://openapi.youdao.com/api"
FROM="zh_CHS"
TO="EN"
APPID="7917fa6b0afb4b56"
APPKEY="NN2kirWKzfavjFnOHZnn0suaMHbC5wS4"
SALT="2"
header_dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

# 提取出的中文描述和翻译结果
zh_sentences = []
en_sentences = []

# 要写入的json格式文件
en_pjson = {
    "sentences": []
}

en_caption_pjson = {
     "caption": "",
     "sen_id": 9,
     "video_id": ""
 }

# 读取zh文件
with open('zh.json','r') as f:
    zh_json = f.read()
f.close()

# json object --> python object
zh_pjson = json.loads(zh_json)
sentences = zh_pjson["sentences"]

for item in sentences:
    translation = json.loads(ten(item["caption"]))["translation"][0]
    en_sentences.append(translation)
    en_caption_pjson["caption"] = translation
    en_caption_pjson["video_id"] = item["video_id"]
    en_pjson["sentences"].append(copy.deepcopy(en_caption_pjson))

# python object --> json object
en_json = json.dumps(en_pjson,ensure_ascii=False)

# write to file
save_to_file("en.json",en_json)

# 打印翻译结果
for sentence in en_sentences:
    print("en: "+sentence)

