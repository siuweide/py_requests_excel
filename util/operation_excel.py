import xlrd



class OperationExcel():

    def __init__(self, file_name='../dataconfig/test1.xlsx', index=0):
        self.open_excel = xlrd.open_workbook(file_name)
        self.excel_sheet = self.open_excel.sheet_by_index(index)

    def get_nrows(self):
        # 获取总行数
        nrows = self.excel_sheet.nrows
        return nrows

    def get_ncols(self):
        # 获取总列数
        nclos = self.excel_sheet.ncols
        return nclos

    def get_cell_value(self, row, col):
        # 获取某个单元格的数据
        data = self.excel_sheet.cell_value(row,col)
        return data

    def get_cols(self, index):
        # 获取某一列的所有数据
        cols = self.excel_sheet.col_values(index)
        return cols

    def get_rows_num(self, cols_id):
        # 根据id获取行号
        num = 0
        cols = self.get_cols(0)
        for id in cols:
            if id == cols_id:
                return num
            num += 1

    def get_rows_value(self,cols_id):
        # 根据id获取某一列的内容
        rows_id = self.get_rows_num(cols_id)
        rows = self.excel_sheet.row_values(rows_id)
        return rows




if __name__ == '__main__':
    test = OperationExcel()
    print(test.get_rows_id('case_02'))