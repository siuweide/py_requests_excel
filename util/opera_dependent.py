import json

from jsonpath_rw import parse

from base.run_main import RunMethod
from data.get_data import GetData
from util.operation_excel import OperationExcel

class OperaDependent():

    def __init__(self, case_id):
        self.case_id = case_id
        self.get_data = GetData()
        self.opera_excel = OperationExcel()
        self.run_case = RunMethod()

    def run_dependent_case(self):
        # 执行依赖的用例
        row_num = self.opera_excel.get_rows_num(self.case_id)
        url = self.get_data.get_url(row_num)
        method = self.get_data.get_method(row_num)
        cookie = self.get_data.is_cookie(row_num)
        if cookie == 'read':
            cookie = self.get_data.read_cookie()
        data = self.get_data.get_headers_data(row_num)
        res = self.run_case.run_main(url=url, headers=cookie, method=method, params=data, data=data)
        return json.loads(res.text)

    def get_data_for_key(self, row):
        depend_data = self.get_data.get_dependent_data(row)
        response_data = self.run_dependent_case()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

if __name__ == '__main__':
    test = OperaDependent('case_02')
    result = test.get_data_for_key(3)
    print(result)