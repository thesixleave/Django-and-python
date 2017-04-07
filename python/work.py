import pandas as pd
from numpy import pmt
url="http://pip.moi.gov.tw/V2/C/SCRC0103.aspx?id=124"
df=pd.read_html(url)

df1=pd.DataFrame(df[0])
df1.to_excel('tess.xlsx')

df2=pd.read_excel('tess.xlsx')

kk=df2.ix[12,1][3:7]


summ=float(7000000)
n=20*12
k=(float(kk)/100)/12
for x in range(n+1):
    list=[x for x in range(n+1)]
df=pd.DataFrame(index=list)
df.insert(0,"期數","")
df.insert(1,"期初金額","")
df.insert(2,"每期支付額","")
df.insert(3,"利息費用","")
df.insert(4,"本金償還","")
df.insert(5,"期末欠款","")

df.to_excel('work.xlsx')

df1=pd.read_excel('work.xlsx')


asum=float(0)
kc=0 ##利息費用
ec=0 ##每期支付額
cc=0 ##本金償還
nc=0 ##期末欠款
len=[" " for x in range(n+1)]
for x in range(n+1):
    
      if x==0:

         df1.ix[x,'期數']=x 
         df1.ix[x,'期末欠款']=nc 
         asum=summ
         df1.ix[x,'期末欠款']=asum
      elif x!=0:
           df1.ix[x,'期數']=x 
           if ec > nc and x>1:
              
              cc=nc
              
           else:
              ec=abs(round(pmt(k,float(n),summ),0))
                 
           kc=round(asum*k,0)
           cc=ec-kc
           nc=asum-cc
           df1.ix[x,'期初金額']=asum
           df1.ix[x,'每期支付額']=ec
           df1.ix[x,'利息費用']=kc
           df1.ix[x,'本金償還']=cc
           
           if nc > 0 and x!=n:
             
              df1.ix[x,'期末欠款']=nc   
           else:
              nc=0
              df1.ix[x,'期末欠款']=nc   
           
           asum=nc


print(df1,kk)
df1.to_excel('work.xlsx')
           

