import pandas as pd                          
from pandas_datareader import data, wb
import pandas_datareader as pdr                
import datetime as dt                        
import time as t
def math():                                  ##將以下的程式 儲存為函式
 print(end='輸入起始日期:')
 instart=input('')                           ##輸入起始日期
 print(end='輸入結束日期:')
 inend=input('')                             ##輸入結束日期
 start = t.strptime(instart, "%Y/%m/%d")     ##輸入格是為西元年/月/日
 end = t.strptime(inend, "%Y/%m/%d")
 start = dt.date(start[0],start[1],start[2]) 
 end = dt.date(end[0],end[1],end[2])
 delta = dt.timedelta(days=1)
 print(end='輸入基金代號:')
 s=input('')
 s=s+'.tw'
 df = pdr.get_data_yahoo(s,start,end)  ##前面為股票代號與國家位置
 da=pd.DataFrame(df)
 da.insert(6,column='單筆',value=' ')      ##新增 欄位名稱
 da.insert(7,column='定期定額',value=' ')
 da.insert(8,column='不定額',value=' ')
 ex1 = 0                    ##表格長度從 0 開始
 ex2 = 1                    ##表格長度從 1 開始
 sum1 = 0                   ##單筆投資的加總變數
 sum2 = 0                   ##定期投資的加總變數
 sum3 = 0                   ##不定額投資的加總變數
 netvalue=0                 ##儲存計算的淨值
 netvalue2=0                 ##儲存上個月的淨值
 md = da.ix[0]['Close']      ##取沒有取道的 1月初 做淨值計算
 while ex2 < len(da):        ##以長度 1 的變數跑 excel的長度
     m1=da.index[ex1].month  ## m1 存取 從 一開始 到最後的日期 月份
     m2=da.index[ex2].month  ## m2 存取 從 一開始+1 到最後的日期 月份
     ex1=ex1+1
     ex2=ex2+1
     if m1 != m2 :                     ##若 有不同的月份 取出
         clo=da.ix[ex1-1]['Close']
         sum1=clo*200000                      ##計算單筆投資
         da.ix[ex1-1, '單筆'] = sum1
         sum2=clo*3000+sum2                  ##計算定額投資
         da.ix[ex1-1, '定期定額'] = sum2
         netvalue=(clo-md)/md                 ##計算淨值
         md=da.ix[ex1]['Close']
         if (netvalue-netvalue2)*100 >10 :  ##如果 大於 10% 減少投資1000元
            sum3=md*(3000-1000)+sum3
            da.ix[ex1-1, '不定額'] = sum3
         elif (netvalue-netvalue2)*100 < -10:  ##如果 小於 10% 增加投資 1000元
            sum3=md*(3000+1000)+sum3
            da.ix[ex1-1, '不定額'] = sum3
         else:                                ##沒有小於 大於 就不變動
            sum3=md*3000+sum3
            da.ix[ex1-1, '不定額'] = sum3
         netvalue2=netvalue                   ##存取上個月淨值的資料
 print(da)   
 df.to_excel('finance.xlsx')##存取抓取的資料為 finance.xlsx
math()
