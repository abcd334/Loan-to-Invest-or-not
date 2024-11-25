# Comparison of Leveraged Investment and Direct Investment Returns: Can Borrowing Yield Higher Profits?
## This study aims to compare the profitability of two approaches, "leveraged investment" and "direct investment without borrowing," using statistical tests to evaluate whether there is a significant difference between the two.

### Methods and Simulation Design
1. Random Price Simulation：
Simulated the price fluctuations of investment assets by generating a sequence of random prices to reflect market dynamics. This approach further evaluates the impact of price volatility on compound returns.

2. Dollar-Cost Averaging Investment：
Calculated the compound effects of regular, fixed investments.

    - Direct Investment (Without Borrowing): Invested a fixed amount monthly.
    - Leveraged Investment (With Borrowing): Invested a fixed amount monthly while also repaying the loan. If the loan repayment exceeded available funds, a portion of the investment units was redeemed to cover the repayments.

3. Return Calculation：
After the loan period, calculated the total investment units and dividends accumulated at the end of the term, converting these into total final returns.

4. Statistical Analysis：
Conducted 1,000 simulations and applied a T-test to analyze whether the total returns of the two approaches showed significant differences.

### Case Study Simulation
1. Case Settings
    - Loan Amount: 1,500,000
    - Loan Term: 36 months
    - Annual Loan Interest Rate: 3%
    - Monthly Repayment: 43,621.81
    - Monthly Fixed Investment: 10,000
    - Annual Investment Return Rate: 3%
    - Dividend Frequency: Quarterly

2. Simulation Results：
    - Average Return Without Borrowing: 370,070.98
    - Average Return With Borrowing: 348,006.59

### Results and Findings

- Simulation Results：
After 1,000 simulations, the T-test results indicated no significant difference in total returns between the "leveraged investment" and "direct investment without borrowing" approaches.

- Conclusion：

    - Leveraged investment did not provide a significant advantage in profitability.
    - Over longer loan repayment periods, the average return of the direct investment approach was significantly higher than that of the leveraged approach.


# 槓桿投資與直接投資的收益比較：貸款是否能帶來更高回報？
## 本研究旨在比較「貸款投資」與「不貸款直接投資」兩種方案的獲利情況，並利用統計檢定評估其間是否存在顯著差異。

### 方法與模擬設計
1. 隨機價格模擬：
模擬投資商品的價格波動，生成隨機價格序列，以反映市場價格的動態變化，進一步評估價格波動對複利收益的影響。

2. 定期定額投入：
計算定期定額投資所產生的複利效果。

    - 不貸款方案：每月定額投入進行投資。
    - 貸款方案：每月定額投入，並支付貸款還款額。若貸款還款金額超出可支配資金，則贖回部分投資單位數用於還款。

3. 收益計算：
在貸款期滿後，計算期末累積的投資單位數以及獲得的配息，並將其轉換為期末總收益。

4. 統計分析：
重複進行 1000 次模擬，利用 T 檢定分析兩方案的期末總收益是否具有顯著差異。

### 實際模擬案例
1. 案例設定
    - 貸款金額：1,500,000
    - 貸款期數：36 期
    - 貸款年利率：3%
    - 每期還款金額：43,621.81
    - 每月定額：10,000
    - 投資年報酬率：3%
    - 配息頻率：季配息

2. 模擬結果：
    - 未貸款方案平均收益：370,070.98
    - 貸款方案平均收益：348,006.59

### 結果與發現

- 模擬結果：
模擬 1000 次後，統計檢定結果顯示「貸款投資方案」與「不貸款方案」的總收益沒有顯著差異。

- 結論：

    - 貸款投資無法取得明顯的額外獲利優勢。
    - 隨著還款期限的延長，未貸款方案的平均收益顯著高於貸款方案。
