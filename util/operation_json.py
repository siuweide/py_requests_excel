import json

class OperationJson():

    def __init__(self, json_file = '../dataconfig/wanyilian.json'):
        self.json_file = json_file


    def read_data(self):
        """ 打开且阅读json文件 """
        with open(self.json_file) as f:
            data = json.load(f)
            return data

    def get_data(self,keyword):
        data = self.read_data()[keyword]
        return data

if __name__ == '__main__':
    test = OperationJson()
    print(test.get_data('event_list'))