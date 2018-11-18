# _*_ coding:utf-8 _*_

import argparse
import re
import traceback
import xlwt
import time
import datetime

def parse_task(line, flag):
    if flag == 'start':
        reg = r'^(\d{2}\/\d{2}\s{1}\d{2}:\d{2}:\d{2},\d{3})\s+:\s+ACTION\s+(.+)\[started\]'
    elif flag == 'finished':
        reg = r'^(\d{2}\/\d{2}\s{1}\d{2}:\d{2}:\d{2},\d{3})\s+:\s+ACTION\s+(.+)\[finished\]'
    m = re.match(reg, line)
    if m:
        # print(m.groups())
        ts =  m.group(1)
        ts = ts.replace(',', '.')
        ts =  str(datetime.datetime.now().year) + '/'+ ts
        t = time.mktime(time.strptime(ts,"%Y/%m/%d %H:%M:%S.%f"))
        action = m.group(2)
        return (action.strip(),t)
    return (None, None)


def load_logs(file_name):
    """ Loading input log file
    :param file_name: the path of the input csv file.
    :return: a new content list
    """

    with open(file_name, 'r', encoding ='utf-8') as input:
        isStart = True
        res = []
        for line in input.readlines():
            if isStart:
                sa, st = parse_task(line, 'start')
                if sa and st:
                    isStart =False
            else:
                fa, ft = parse_task(line, 'finished')
                if fa and ft:
                    isStart =True
                if sa and st and fa and ft and sa == fa:
                    res.append((sa, ft-st))
    return res

def get_style(forecolor, bold):
    """Generate a style for specified forecolor and has bold or not
    :param forecolor: the name of the forecolor.
    :param bold: has bold or not.
    :return: a style, an :class:`XFstyle` object.
    """
    # https://secure.simplistix.co.uk/svn/xlwt/trunk/xlwt/Style.py
    # https://www.crifan.com/python_xlwt_set_cell_background_color/
    style = xlwt.easyxf(
        'pattern: pattern solid, fore_colour %s; font: bold %s;' % (
            forecolor, bold))
    return style

def export_xls(content, file_name):
    """Exporting the content into sa xls file as a specific format
    :param content: the content loaded from csv file.
    :param file_name: the path of the output xls file.
    """
    excel_file = xlwt.Workbook(encoding='utf8')
    new_sheet = excel_file.add_sheet('raw-data', cell_overwrite_ok='True')
    style = get_style('aqua', 'on')
    new_sheet.write(0, 0, 'Action Name', style)
    new_sheet.write(0, 1, 'Action Duration', style)
    for row_num, row in enumerate(content):
        for col_num, column in enumerate(row):
            if col_num> 0 and float(column) > 2.0:
                style = get_style('yellow', 'off')
            else:
                style = xlwt.Style.default_style
            new_sheet.write(row_num+1, col_num, column, style)

    excel_file.save(file_name)

def process_arg():
    """Processing input arguments

    : return: input args, has to be an instance of : attr: `argparse.Namespace`.
    """
    parse = argparse.ArgumentParser(prog = 'log2Excel', allow_abbrev=True)
    parse.add_argument('--input', '-i', help ='The file path of input file', required = True)
    parse.add_argument('--output', '-o', help ='The file path of output file', required= True)
    return parse.parse_args()

if __name__ == '__main__':
    try:
        arg = process_arg()

        content = load_logs(arg.input)
        export_xls(content, arg.output)
    except Exception as exp:
        print(exp)
        traceback.print_exc()