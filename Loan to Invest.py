import numpy as np
import random as rd
import pandas as pd
from scipy import stats

#貸款金額
Loan_amount=1500000
#貸款期數/月
Loan_period=36
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

data=pd.DataFrame()

for sample in range(1,1000):
    QTY_No_Loan = round(Invest_Amount / price, 2)
    QTY_Loan = round((Loan_amount + Invest_Amount) / price, 2)
    Acc_Pay_No_Loan = 0
    Acc_Pay_Loan = 0
    Pay_No_Loan = 0
    Pay_Loan = 0
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

        else: #沒配息
            # 無貸款的計算
            QTY_No_Loan += round((Invest_Amount) / price, 2)
            # 貸款的計算
            QTY_Loan += round((Invest_Amount + monthly_pay) / price, 2)

    data=data.append({'No': '第'+str(sample)+'次','未貸款期末單位數':round(QTY_No_Loan,2),'貸款期末單位數':round(QTY_Loan,2),
          '未貸款期末本金':round((QTY_No_Loan*Expect_Price_Ave),2),'貸款期末本金':round((QTY_Loan*Expect_Price_Ave),2),
          '未貸款累積配息':round(Acc_Pay_No_Loan,2),'貸款累積配息':round(Acc_Pay_Loan,2)
          }, ignore_index=True)
print(data)

ave_no_loan_amt=sum(data['未貸款期末本金']) / sample
ave_loan_amt=sum(data['貸款期末本金']) / sample
ave_no_loan_dvd=sum(data['未貸款累積配息']) / sample
ave_loan_dvd=sum(data['貸款累積配息']) / sample

statistic, p_value = stats.ttest_ind((data['未貸款期末本金']+data['未貸款累積配息']),(data['貸款期末本金']+data['貸款累積配息']))

if p_value<0.05:
    print('貸款',Loan_amount,'    期數', Loan_period, '     每期還款金額', monthly_pay)
    print('模擬'+str(sample)+'次後，兩方案有明顯差異')
    print('經過'+str(Loan_period)+'期後')
    if (ave_no_loan_amt+ave_no_loan_dvd)>(ave_loan_amt+ave_loan_dvd):
        print('平均未貸款方案可多賺',round((ave_no_loan_amt-ave_loan_amt+ave_no_loan_dvd-ave_loan_dvd),2))
    elif (ave_no_loan_amt+ave_no_loan_dvd)<(ave_loan_amt+ave_loan_dvd):
        print('平均貸款方案可多賺', round((ave_loan_amt - ave_no_loan_amt+ave_loan_dvd-ave_no_loan_dvd), 2))
else:
    print('貸款', Loan_amount, '    期數', Loan_period, '     每期還款金額', monthly_pay)
    print('模擬'+str(sample)+'次後，兩方案沒有明顯差異')
    print('經過' + str(Loan_period) + '期後')
    print('未貸款方案平均收益為',round((ave_no_loan_amt),2))
    print('貸款方案平均本金為',round((ave_loan_amt),2))