'''
Created on 2018-11-08

'''
import csv
import os, glob
import sys
import xlsxwriter

if __name__ == '__main__':
    listOfFiles = glob.glob("*.txt")                       
    for index, fileInList in enumerate(listOfFiles):     
        fileName  = fileInList[0:fileInList.find('.')]     
        excelFile = xlsxwriter.Workbook(fileName + '.xlsx')
        worksheet = excelFile.add_worksheet()    

        with open(fileInList, 'rb', encoding="utf-8", newline="\r\n" ) as f:   
            content = csv.reader(f)
            for index_row, data_in_row in enumerate(content):
                for index_col, data_in_cell in enumerate(data_in_row):
                    worksheet.write(index_row, index_col, data_in_cell)
    
        excelFile.close()
    print(" === Conversion is done ===")
