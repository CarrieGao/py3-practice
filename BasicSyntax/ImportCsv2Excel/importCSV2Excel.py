'''
Created on 2018-11-08

'''
import csv
import os
import glob
import sys

# Xlwt 模块有一个bug， 就是所用样式过多的话，之后的数据将使用不了样式，相反xlsxwriter 模块 不会有此问题。
# 用Xlwt模块的同学们，请务必转换用xlsxwriter模块 !!!!!!
import xlsxwriter
from xlrd import open_workbook


def getHeaderFormat(workbook):
    props = {
        'bold': True,
        'bg_color': 'blue'
    }
    return workbook.add_format(props)

# out of stock format


def getOutOfStockFormat(workbook):
    props = {
        'bg_color': 'yellow'
    }
    return workbook.add_format(props)

# out of stock format


def getVoidFormat(workbook):
    props = {
        'bg_color': 'red'
    }
    return workbook.add_format(props)


def filterEmptyLine(data):
    result = []
    for item in enumerate(data):
        if len(item) > 0:
            result.append(item)
    return result


def comparator(tupleElem):
    return tupleElem[1]


if __name__ == '__main__':
    dir = os.path.join(
        "C:\Carrie\Python_learn\py3-practice\BasicSyntax\ImportCsv2Excel\InputFiles", '*.txt')
    listOfFiles = glob.glob(dir)
    for index, fileInList in enumerate(listOfFiles):
        fileName = fileInList[0:fileInList.find('.')]
        excelFile = xlsxwriter.Workbook("fileName" + '.xlsx')
        worksheet = excelFile.add_worksheet("库存状态")

        with open(fileInList, 'r', encoding="UTF-8", newline="\n") as f:
            # content= f.readlines()
            content = csv.reader(f, delimiter='，')
            # filterContent = filterEmptyLine(content)
            # filter out empty line
            row = 0
            for index_row, data_in_row in enumerate(content):
                    if len(data_in_row) > 0:
                        for index_col, data_in_cell in enumerate(data_in_row):
                            # process header
                            if row == 0:
                                worksheet.write(row, index_col,
                                                data_in_cell, getHeaderFormat(excelFile))
                            # process data
                            elif index_col == 1:
                                worksheet.write(
                                    row, index_col, data_in_cell, getOutOfStockFormat(excelFile))
                            else:
                                worksheet.write(row, index_col, data_in_cell)
                        row = row + 1
        excelFile.close()
    print(" === Conversion is done ===")
