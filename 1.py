import pymysql
import pandas as pd
from WindPy import w
con = pymysql.connect(host='192.168.1.198', db='wind_dev', user='windqueryuser', password='sfe34sjkegd', charset='utf8')
sql = 'select S_INFO_WINDCODE, TRADE_DT, PE_TTM from wind_dev.aindexvaluation where S_INFO_WINDCODE="000300.SH" ' \
      'order by TRADE_DT'
data = pd.read_sql(sql, con)
print(data.iloc[-1:])

w.start()
dt = w.wsd('000300.SH', 'pe_ttm', '2004-06-01', '2018-07-25', '')
df = pd.DataFrame(dt.Data).T
ti = pd.to_datetime(dt.Times)
df.index = ti
print(df.loc['2018-05-31'])
