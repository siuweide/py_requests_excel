from base.run_main import RunMethod
from data.get_data import GetData
from util.opera_dependent import OperaDependent
from util.operation_excel import OperationExcel
from util.verify_result import verify_str
from util.send_email import sendEmail


class RunTest():

    def __init__(self):
        self.get_data = GetData()
        self.oprea = OperationExcel()
        self.run = RunMethod()

    def go_on_run(self):
        # 先获取总共的行数
        success_count = []
        fail_count = []
        nrows = self.oprea.get_nrows()
        for i in range(1, nrows):
            is_run = self.get_data.get_is_run(i)
            if is_run:
                url = self.get_data.get_url(i)
                method = self.get_data.get_method(i)
                cookie = self.get_data.is_cookie(i)
                data = self.get_data.get_headers_data(i)
                depend_case = self.get_data.get_dependent_id(i)
                expected_result = self.get_data.get_expected_result(i)
                if cookie == "write":
                    # 1、执行用例
                    result = self.run.run_main(url=url, method=method, params=data, data=data)
                    # 2、将结果写入到到user_json_cookie.json文件
                    self.get_data.write_json_cookie(result)
                    result = result.text
                    if verify_str(expected_result, result):
                        self.get_data.write_actual_result(i+1, 'pass')
                        success_count.append(i)
                    else:
                        self.get_data.write_actual_result(i+1, 'fail')
                        fail_count.append(i)
                elif cookie == "read":
                    # 1、读取cookie数据，且把cookie传入到header中
                    cookie = self.get_data.read_cookie()
                    if depend_case != '':
                        opera_depent = OperaDependent(depend_case)
                        # 根据依赖数据的字段，返回对应的数据
                        get_depend_data = opera_depent.get_data_for_key(i)
                        # 获取依赖数据所属字段
                        depend_key = self.get_data.get_dependent_field(i)
                        # 将依赖的数据，赋值到依赖数据所属字段
                        data[depend_key] = get_depend_data
                    print('cookie-------->',cookie)
                    result = self.run.run_main(url=url, method=method, params=data, data=data, headers=cookie).text
                    if verify_str(expected_result, result):
                        self.get_data.write_actual_result(i + 1, 'pass')
                        success_count.append(i)
                    else:
                        self.get_data.write_actual_result(i + 1, 'fail')
                        fail_count.append(i)
        count_case = len(success_count) + len(fail_count)
        sendEmail(count_case, success_count, fail_count)

if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()