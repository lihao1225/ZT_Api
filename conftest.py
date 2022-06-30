"""
Author: lihao
Time: 2022/6/6

"""
import os

import pytest

from common.handle_path import DIR
from common.yaml_util import YamlUtil


@pytest.fixture(scope='session',autouse=True)
def clear_extract():
    YamlUtil(os.path.join(DIR,'extract.yaml')).clear_yaml()
