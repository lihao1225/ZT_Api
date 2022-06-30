"""
Author: lihao
Time: 2022/5/31

"""
import os

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONF = os.path.join(DIR,'config')
LOG = os.path.join(DIR,'logs')
YAML_DATA = os.path.join(DIR,'case_yaml')