from data_fetch import *

def search_stock(ticker):
    '''
    输入股票名称，返回详细股票信息
    用于股票查询，或点击股票跳转到详细股票信息展示页面
    '''
    data = get_real_time_data(ticker)
    result = None
    for k in data['stock_info'].keys():
        if k == 'companyOfficers' or k == 'longBusinessSummary':
            continue
        info = k + (28-len(k))*' ' + str(data['stock_info'][k])
        result += (info + '\n')
    result += ('longBusinessSummary:\n' + data['stock_info']['longBusinessSummary'] +'\ncompanyOfficers:')
    for person in data['stock_info']['companyOfficers']:
        result += (person["name"] + '\n')
    return result

def search_person(name):
    '''
    输入人名，返回详细个人信息
    可以用于实现在详细股票信息中点击companyOfficers名字跳转到详细个人信息展示页面
    '''
    for person in data['stock_info']['companyOfficers']:
        if name == person["name"]:
            return person
    