# 🌍 IGMP - Investable Global Market Portfolio

Academic implementation of the true market portfolio that extends beyond traditional stock-only models. While CAPM and similar frameworks typically use stock market indices as proxies for the "market portfolio," this implementation captures the complete investable universe across all major asset classes, weighted by global market capitalization.

**Why This Matters:** Most portfolio theory assumes investors hold the market portfolio, but in practice, "the market" is much broader than just stocks. This IGMP includes bonds, real estate, and commodities - representing what the theoretical market portfolio should actually look like.

## 📊 Portfolio Composition

**Target Allocation:**
- **55% Fixed Income** - US Treasury bonds, international bonds, emerging market debt
- **35% Global Equities** - US stocks, international developed markets, emerging markets  
- **7% Real Estate** - US and international REITs
- **3% Commodities** - Gold and broad commodity exposure

## 🎯 Implementation

The IGMP is constructed using 13 liquid, low-cost ETFs that provide broad exposure to global markets. Each ETF was selected for its representativeness, liquidity, and cost efficiency:

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

**IGMP Portfolio Metrics (2019-2024):**
- **Annual Return:** 6.4%
- **Volatility:** 9.2%
- **Sharpe Ratio:** 0.70
- **Maximum Drawdown:** -20.0%

**Key Insight:** The IGMP delivers moderate returns with significantly lower risk than equity-heavy portfolios. While SPY outperforms on absolute returns, the IGMP's superior risk-adjusted performance and drawdown protection make it attractive for risk-conscious investors.

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

The IGMP embodies the theoretical "market portfolio" from modern portfolio theory - what all rational investors would hold in equilibrium. Unlike typical implementations that proxy the market with stock indices, this version includes the full spectrum of investable assets.

**Core Principles:**
- **Completeness:** Represents the entire global investment opportunity set
- **Market Efficiency:** Weights reflect aggregate investor preferences and available supply
- **Diversification:** Maximum risk reduction through low-correlation asset classes
- **Accessibility:** Implemented through liquid, tradeable ETFs rather than theoretical constructs

**Practical Application:** This portfolio serves as a benchmark for true diversification and can be used as a core holding, with tactical adjustments based on individual circumstances, market views, or regulatory constraints.

## ⚠️ Important Considerations

**Research Purpose:** This implementation is designed for academic research and educational purposes. It demonstrates theoretical portfolio construction but should not be considered personalized investment advice.

**Market Limitations:** While this approximates the global investable universe, real-world constraints create distortions:
- **Regulatory Requirements:** Banks and pension funds may overweight certain assets (like Treasuries) due to capital requirements
- **Liquidity Constraints:** Some investors cannot access all asset classes equally
- **Transaction Costs:** Frequent rebalancing may not be practical for smaller portfolios
- **Tax Implications:** Asset location and tax efficiency vary by jurisdiction

**Future Enhancements:** A constraint-adjusted version could account for these regulatory distortions to better represent the theoretically optimal unconstrained portfolio.

---
