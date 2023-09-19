"""
用于文件相关定义
"""
import json

from data_define import Record


class FileReader:  # 抽象类

    def read_data(self) -> list[Record]:
        """用于读取相关文件 抽象类"""
        pass


class TextReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        with open(self.path, 'r', encoding='UTF-8') as f:
            record = []
            for line in f.readlines():
                file_data = line.strip().split(',')
                record.append(Record(file_data[0], file_data[1], int(file_data[2]), file_data[3]))

        return record


class JsonReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        with open(self.path, 'r', encoding='UTF-8') as f:
            record = []
            for line in f.readlines():
                data_dict = json.loads(line)
                record.append(
                    Record(data_dict['date'], data_dict['order_id'], data_dict['money'], data_dict['province']))
        return record


if __name__ == '__main__':
    text1 = TextReader('D:/dev/python-learn/2011年1月销售数据.txt')
    text2 = JsonReader('D:/dev/python-learn/2011年2月销售数据JSON.txt')

    list1 = text1.read_data()
    list2 = text2.read_data()

    for l in list1:
        print(l)
    for l in list2:
        print(l)
