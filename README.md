# 🌍 IGMP - Investable Global Market Portfolio

Academic implementation of the "buy everything" portfolio strategy based on global market capitalization weights. This project builds a truly diversified portfolio representing the entire investable universe.

## 📊 Portfolio Composition

**Target Allocation:**
- **55% Fixed Income** - US Treasury bonds, international bonds, emerging market debt
- **35% Global Equities** - US stocks, international developed markets, emerging markets  
- **7% Real Estate** - US and international REITs
- **3% Commodities** - Gold and broad commodity exposure

## 🎯 Implementation

The IGMP is constructed using 13 globally diversified ETFs with low fees:

### Fixed Income (55%)
- **AGG** (20%) - US Aggregate Bonds
- **VXUS** (15%) - International Bonds  
- **EMB** (10%) - Emerging Market Bonds
- **TIPS** (10%) - Inflation-Protected Securities

### Global Equities (35%)
- **SPY** (15%) - S&P 500 (US Large Cap)
- **VTI** (10%) - US Total Stock Market
- **VEA** (7%) - Developed Markets International
- **VWO** (3%) - Emerging Markets

### Real Estate (7%)
- **VNQ** (4%) - US REITs
- **VNQI** (3%) - International REITs

### Commodities (3%)
- **GLD** (2%) - Gold
- **DJP** (1%) - Broad Commodities

## 📈 Performance Results

**IGMP Portfolio Metrics (Backtest Period):**
- **Annual Return:** 6.4%
- **Volatility:** 9.2% 
- **Sharpe Ratio:** 0.70
- **Maximum Drawdown:** -20.0%

**Benchmark Comparison:**
| Portfolio | Annual Return | Volatility | Sharpe Ratio | Max Drawdown |
|-----------|---------------|------------|--------------|--------------|
| **IGMP**  | 6.4%         | 9.2%       | **0.70**     | -20.0%       |
| SPY       | 14.3%        | 17.9%      | 0.80         | -33.7%       |
| VT        | 11.5%        | 17.2%      | 0.67         | -34.2%       |
| BND       | 2.1%         | 5.4%       | 0.38         | -18.6%       |

## 🚀 Key Benefits

1. **Global Diversification** - Exposure to all major asset classes and geographic regions
2. **Risk Management** - Lower volatility than pure equity portfolios
3. **Academic Foundation** - Based on modern portfolio theory and market efficiency research
4. **Rebalancing Strategy** - Systematic rebalancing maintains target allocations
5. **Low Correlation** - Diversified across uncorrelated asset classes

## 📊 Risk Analysis

- **Correlation Benefits:** The portfolio shows low correlation between asset classes
- **Drawdown Protection:** Significantly lower maximum drawdown than equity-only strategies  
- **Volatility Management:** 9.2% volatility vs 17.9% for SPY
- **Steady Performance:** More consistent returns with less dramatic swings

## 🛠️ Usage

Run the analysis:
```python
python3 igmp.py
```

This generates:
- Performance metrics and Sharpe ratio comparisons
- Risk-return scatter plot with annotations
- Sharpe ratio comparison bar chart
- Rolling performance analysis

## 📚 Academic Foundation

Based on research from:
- **Doeswijk, Lam & Swinkels (2014):** "The Global Multi-Asset Market Portfolio"
- **Siegel & Bodie (2000):** "Global Investment Performance"
- **Markowitz (1952):** Modern Portfolio Theory

## 💡 Investment Philosophy

The IGMP represents the optimal market portfolio that all investors would hold in a perfect world with no constraints. It provides:

- **Market Efficiency:** Captures returns from all investable assets
- **Diversification:** Maximum risk reduction through correlation benefits
- **Simplicity:** Single portfolio solution for global exposure
- **Academic Rigor:** Theoretically sound allocation methodology

## ⚠️ Important Notes

- Past performance does not guarantee future results
- This is for educational/research purposes only
- Not personalized investment advice
- Consider your own risk tolerance and investment objectives
- This "World Portfolio" is a good approximation of the global asset allocation, but it might be interesting to adjust it for constrained buyers that overweight some assets (such as Treasuries) for regulatory reasons so it better represents the efficient portfolio.

---
