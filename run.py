"""
Author: lihao
Time: 2022/6/6

"""
import os

import pytest

from common.handle_path import YAML_DATA

if __name__ == '__main__':
    pytest.main(["-vs","./test_cases/test_api.py"])
    os.system("allure generate ./temps -o ./reports --clean")

