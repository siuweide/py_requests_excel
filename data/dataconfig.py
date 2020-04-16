from util.operation_excel import OperationExcel


class Excel_col():
    id = 0
    url = 1
    is_run = 2
    method = 3
    headers = 4
    dependent_id = 5
    dependent_data = 6
    dependent_field = 7
    data = 8
    expected_result = 9
    actual_result = 10

def global_id():
    """ 获取id """
    return Excel_col.id

def global_url():
    """ 获取url """
    return Excel_col.url

def global_is_run():
    """ 获取是否运行 """
    return Excel_col.is_run

def global_method():
    """ 获取请求方法 """
    return Excel_col.method

def global_headers():
    """ 获取headers """
    return Excel_col.headers

def global_dependent_id():
    """ 获取依赖的id """
    return Excel_col.dependent_id

def global_dependent_data():
    """ 获取依赖的数据 """
    return Excel_col.dependent_data

def global_dependent_field():
    """ 获取依赖数据的字段 """
    return Excel_col.dependent_field

def global_data():
    """ 依赖数据所属字段 """
    return Excel_col.data

def global_expected_result():
    """ 获取预期结果 """
    return Excel_col.expected_result

def global_actual_result():
    """ 获取实际结果 """
    return Excel_col.actual_result

if __name__ == '__main__':
    operation = OperationExcel()
    url = operation.get_cell_value(1,global_url())
    is_run = operation.get_cell_value(1, global_is_run())
    print(is_run)