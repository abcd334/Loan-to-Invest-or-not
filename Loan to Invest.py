import numpy as np
import random as rd
import pandas as pd
from scipy import stats

#貸款金額
Loan_amount=100000
#貸款期數/月
Loan_period=30
#貸款年利息%
Loan_rate=3

#每月投入金額
Invest_Amount=10000
#投資年報酬率%
Invest_rate=5
#幾個月配息一次
Invest_period=3
#投資商品預期價格區間
Expect_Price_Low=15
Expect_Price_High=25


Expect_Price_Ave=(Expect_Price_High+Expect_Price_Low)/2
monthly_pay=np.pmt(Loan_rate/12/100, Loan_period, Loan_amount).round(2)
price=round(rd.uniform(Expect_Price_Low,Expect_Price_High),2)

QTY_No_Loan = round(Invest_Amount / price,2)
QTY_Loan = round((Loan_amount+Invest_Amount) / price,2)
QTY_No_Loan_Max = round(Invest_Amount / Expect_Price_Low,2)
QTY_No_Loan_Min = round(Invest_Amount / Expect_Price_High,2)
QTY_Loan_Max = round((Loan_amount+Invest_Amount) / Expect_Price_Low,2)
QTY_Loan_Min = round((Loan_amount+Invest_Amount) / Expect_Price_High,2)

Acc_Pay_No_Loan=0
Acc_Pay_Loan=0
history=pd.DataFrame()
Pay_No_Loan=0
Pay_Loan=0

history = history.append(
        {'期數': 1,
         '未貸款配息': round(Pay_No_Loan,2), '貸款配息': round(Pay_Loan,2),
         '未貸款單位數': round(QTY_No_Loan,2),'貸款單位數': round(QTY_Loan,2),
         '未貸款本金': round(QTY_No_Loan*Expect_Price_Ave,2),'貸款本金': round(QTY_Loan*Expect_Price_Ave,2),
         '未貸款最大單位數': round(QTY_No_Loan_Max, 2), '貸款最大單位數': round(QTY_Loan_Max, 2),
         '未貸款最大本金': round(QTY_No_Loan_Max * Expect_Price_High, 2), '貸款最大本金': round(QTY_Loan_Max * Expect_Price_High, 2),
         '未貸款最小單位數': round(QTY_No_Loan_Min, 2), '貸款最小單位數': round(QTY_Loan_Min, 2),
         '未貸款最小本金': round(QTY_No_Loan_Min * Expect_Price_Low, 2),
         '貸款最小本金': round(QTY_Loan_Min * Expect_Price_Low, 2)
         }, ignore_index=True)


for period in range(2,Loan_period+1):
    price = round(rd.uniform(Expect_Price_Low,Expect_Price_High),2)

    if period % Invest_period ==0: #有配息
        #無貸款的計算
        Pay_No_Loan = round(QTY_No_Loan * Invest_rate / Invest_period / 100,2) #配息金額
        QTY_No_Loan+= round((Invest_Amount + Pay_No_Loan)/price,2) #配息再投資
        Acc_Pay_No_Loan+=Pay_No_Loan #累積配息
        #貸款的計算
        Pay_Loan=round(QTY_Loan*Invest_rate/Invest_period/100,2) #配息金額
        QTY_Loan += round((Invest_Amount + monthly_pay + Pay_Loan) / price,2) #配息再投資 or 贖回付貸款
        Acc_Pay_Loan+=Pay_Loan #累積配息

        #以最低price計算________________________________________________________________
        # 無貸款的計算
        Pay_No_Loan_Max = round(QTY_No_Loan_Max * Invest_rate / Invest_period / 100, 2)  # 配息金額
        QTY_No_Loan_Max += round((Invest_Amount + Pay_No_Loan_Max) / Expect_Price_Low, 2)  # 配息再投資
        # 貸款的計算
        Pay_Loan_Max = round(QTY_Loan_Max * Invest_rate / Invest_period / 100, 2)  # 配息金額
        QTY_Loan_Max += round((Invest_Amount + monthly_pay + Pay_Loan_Max) / Expect_Price_Low, 2)  # 配息再投資 or 贖回付貸款

        # 以最高price計算________________________________________________________________
        # 無貸款的計算
        Pay_No_Loan_Min = round(QTY_No_Loan_Min * Invest_rate / Invest_period / 100, 2)  # 配息金額
        QTY_No_Loan_Min += round((Invest_Amount + Pay_No_Loan_Min) / Expect_Price_High, 2)  # 配息再投資
        # 貸款的計算
        Pay_Loan_Min = round(QTY_Loan_Min * Invest_rate / Invest_period / 100, 2)  # 配息金額
        QTY_Loan_Min += round((Invest_Amount + monthly_pay + Pay_Loan_Min) / Expect_Price_High, 2)  # 配息再投資 or 贖回付貸款


    else: #沒配息
        # 無貸款的計算
        QTY_No_Loan += round((Invest_Amount) / price, 2)
        # 貸款的計算
        QTY_Loan += round((Invest_Amount + monthly_pay) / price, 2)

        # 以最低price計算________________________________________________________________
        # 無貸款的計算
        QTY_No_Loan_Max += round((Invest_Amount) / Expect_Price_Low, 2)
        # 貸款的計算
        QTY_Loan_Max += round((Invest_Amount + monthly_pay) / Expect_Price_Low, 2)

        # 以最高price計算________________________________________________________________
        # 無貸款的計算
        QTY_No_Loan_Min += round((Invest_Amount) / Expect_Price_High, 2)
        # 貸款的計算
        QTY_Loan_Min += round((Invest_Amount + monthly_pay) / Expect_Price_High, 2)


    # 將資料加入history
     # '期數': period,
    #history.index = '第' + str(period)+'期'
    history = history.append(
        {'期數': period,
         '未貸款配息': round(Pay_No_Loan,2), '貸款配息': round(Pay_Loan,2),
         '未貸款單位數': round(QTY_No_Loan,2),'貸款單位數': round(QTY_Loan,2),
         '未貸款本金': round(QTY_No_Loan*Expect_Price_Ave,2),'貸款本金': round(QTY_Loan*Expect_Price_Ave,2),
         '未貸款最大單位數': round(QTY_No_Loan_Max, 2), '貸款最大單位數': round(QTY_Loan_Max, 2),
         '未貸款最大本金': round(QTY_No_Loan_Max * Expect_Price_High, 2), '貸款最大本金': round(QTY_Loan_Max * Expect_Price_High, 2),
         '未貸款最小單位數': round(QTY_No_Loan_Min, 2), '貸款最小單位數': round(QTY_Loan_Min, 2),
         '未貸款最小本金': round(QTY_No_Loan_Min * Expect_Price_Low, 2),
         '貸款最小本金': round(QTY_Loan_Min * Expect_Price_Low, 2)
         }, ignore_index=True)

data={'期末單位數':[round(QTY_No_Loan,2),round(QTY_Loan,2)],
      '期末本金':[round((QTY_No_Loan*Expect_Price_Ave),2),round((QTY_Loan*Expect_Price_Ave),2)],
      '累積配息':[round(Acc_Pay_No_Loan,2),round(Acc_Pay_Loan,2)],
      }
df = pd.DataFrame(data)
df.index = ["未貸款", "貸款"]

statistic, p_value = stats.ttest_ind(history['未貸款本金'],history['貸款本金'])

print('期數',Loan_period,'  每期還款金額',monthly_pay)
print('______________________________________________________________________________')
print(history)
print('______________________________________________________________________________')
print(df)
print('______________________________________________________________________________')
if (df['期末本金']['未貸款']-df['期末本金']['貸款'])>0:
    print('不貸款約可多賺',round((df['期末本金']['未貸款']-df['期末本金']['貸款']),2))
else:
    print('貸款投資約可多賺',round((df['期末本金']['貸款']-df['期末本金']['未貸款']),2))



'''

print('________________')
print('未貸款期末單位數',round(QTY_No_Loan,2)
print('期末本金',round((QTY_No_Loan*Expect_Price_High),2))
print('________________')
print('貸款期末單位數',round(QTY_Loan,2)
print('期末本金',round((QTY_Loan*Expect_Price_High),2))
print(Pay_No_Loan)
        print(QTY_No_Loan)
        print(Pay_Loan)
        print(QTY_Loan)
        input()
'''