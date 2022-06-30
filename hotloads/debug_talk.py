"""
Author: lihao
Time: 2022/6/2

"""
import os
import random

import yaml

from common.handle_path import DIR, CONF


class DebugTalk:
    # 生成随机数
    def get_random(self, min, max):
        return str(random.randint(int(min), int(max)))

    # 读取提取文件信息
    def read_extract(self, key):
        with open(os.path.join(DIR, 'extract.yaml'), mode='r', encoding='utf-8') as f:
            result = yaml.load(stream=f, Loader=yaml.FullLoader)
            return result[key]

    # 读取配置文件
    def read_config(self, note_key):
        with open(os.path.join(CONF, 'config.yaml'), mode='r', encoding="utf-8") as f:
            res = yaml.load(stream=f, Loader=yaml.FullLoader)
            return res[note_key]
