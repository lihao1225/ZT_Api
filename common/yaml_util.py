"""
Author: lihao
Time: 2022/5/31

"""
import yaml


class YamlUtil:

    def __init__(self, yaml_path):
        """
        :param yaml_path: yaml的文件路径
        """
        self.yaml_path = yaml_path

    def read_yaml(self):
        with open(self.yaml_path, 'r', encoding="utf-8") as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
        return data

    def write_yaml(self, data):
        with open(self.yaml_path, 'w', encoding="utf-8") as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    def clear_yaml(self):
        with open(self.yaml_path, "w", encoding="utf-8") as f:
            f.truncate()
