"""
Author: lihao
Time: 2022/5/31

"""
import datetime
import logging
import os
import time
import yaml

from common.handle_path import CONF, LOG


def error_log(msg):
    LoggerUtil().create_log().error(msg)


def info_log(msg):
    LoggerUtil().create_log().info(msg)


class LoggerUtil:

    def read_config_log(self, log, log_key):
        with open(os.path.join(CONF, 'config.yaml'), 'r', encoding='utf-8') as f:
            res = yaml.load(stream=f, Loader=yaml.FullLoader)
            return res[log][log_key]

    def create_log(self):
        # 创建收集器，设置收集器等级
        mylog = logging.getLogger(self.read_config_log('log', 'log_file_name'))
        mylog.setLevel(self.read_config_log('log', 'log_level'))
        if not mylog.handlers:
            # 创建输出到控制台，设置等级
            sh = logging.StreamHandler()
            sh.setLevel(self.read_config_log('log', 'sh_level'))
            mylog.addHandler(sh)
            # 创建输出到文件，设置等级
            fh = logging.FileHandler(
                filename=os.path.join(LOG, f'log_{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.log'),
                encoding='utf-8')
            fh.setLevel(self.read_config_log('log', 'fh_level'))
            mylog.addHandler(fh)
            # 设置日志输出格式
            formater = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
            fm = logging.Formatter(formater)
            sh.setFormatter(fm)
            fh.setFormatter(fm)
        return mylog
