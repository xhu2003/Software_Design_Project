from data_fetch import *

# def search_stock(ticker):
#     '''
#     输入股票名称，返回详细股票信息
#     用于股票查询，或点击股票跳转到详细股票信息展示页面
#     '''

#     data = get_real_time_data(ticker)
#     if not data or 'stock_info' not in data:
#         return f'No data available for {ticker}.'

#     result = ''
#     for k in data['stock_info'].keys():
#         if k == 'companyOfficers' or k == 'longBusinessSummary':
#             continue
#         info = k + (28 - len(k)) * ' ' + str(data['stock_info'][k])
#         result += (info + '\n')

#         result += ('longBusinessSummary:\n' + data['stock_info']['longBusinessSummary'] + '\ncompanyOfficers:')
#         for person in data['stock_info']['companyOfficers']:
#             result += (person["name"] + '\n')

#         return result
# print(search_stock('msft'))

def get_stock_info(ticker):
    """
    Fetch and return stock information for a given ticker symbol.
    Returns the data in a dictionary format for easy access in templates.
    """
    data = get_real_time_data(ticker)
    if not data or 'stock_info' not in data:
        return None

    relevant_keys = ['symbol', 'shortName', 'longName', 'currentPrice', 'marketCap', 'dayHigh', 'dayLow']
    stock_info_data = data['stock_info']
    stock_info = {}

    # Loop over the relevant keys and fetch their values
    for key in relevant_keys:
        stock_info[key] = stock_info_data.get(key, 'N/A')

    return stock_info


# print(get_stock_info('msft'))
# def search_person(ticker, name):
#     '''
#     输入人名，返回详细个人信息
#     可以用于实现在详细股票信息中点击companyOfficers名字跳转到详细个人信息展示页面
#     '''
#     data = get_real_time_data(ticker)
#     for person in data ['stock_info']['companyOfficers']:
#         if name == person["name"]:
#             return person
    