import pandas as pd
import MySQLdb 
import time
import datetime as dt
import matplotlib.pyplot as plt

print("執行後請等候,因納入資料有點長,故需要一點時間")

df=pd.read_excel('TEJ.xlsx',index = False)
df.rename(columns={'Current':'Code','Unnamed: 1':'Date','Unnamed: 2':'PER'}, inplace=True)
df2=pd.DataFrame(df)

db = MySQLdb.connect(host="db.mis.kuas.edu.tw",user="s1103137227",passwd="3ajilojl",db="s1103137227", charset="utf8")
cur=db.cursor()
sql = """CREATE TABLE TEJ ( 
         Code CHAR(20) NOT NULL,
         Name CHAR(20) NOT NULL,
         Date DATE,
         PER FLOAT )ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"""

cur.execute(sql)



for x in range(2,len(df2.Date)):
    if df2.PER[x] == "-":
       df2.PER[x]=0
    cur.execute("INSERT INTO `tej` (`Code`, `Name`, `Date`, `PER`) VALUES (%s, %s, %s, %s);",(df2.Code[x][0:4],df2.Code[x][4::],df2.Date[x],df2.PER[x]))
db.commit()


sql2="""SELECT Date,sum(PER)/COUNT(*) FROM tej GROUP BY Date HAVING COUNT(*) > 1 or COUNT(*)=1"""

cur=db.cursor()
cur.execute(sql2)

result = cur.fetchall()

df=pd.DataFrame(list(result),columns=["時間","本益比"]);
plt.ylabel('PER')            
plt.xlabel('COUNT')   

print(plt.plot(df['本益比']))

sql3="""DROP TABLE tej"""

cur.execute(sql3)
db.close()


