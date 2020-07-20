# encoding: utf-8

import json

with open('G:/imageFiles/downtown_walkBridge_01/result/image_01371_keypoints.json','r',encoding='utf8') as fp:
    json_data = json.load(fp)
    print(json_data)
    print(json_data.keys())