import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

def get_igmp_portfolio():
    """Define the global market portfolio weights"""
    return {
        # Fixed Income (55%)
        'BND': 0.22,    # US Bonds  
        'BNDX': 0.18,   # International Bonds
        'VWOB': 0.08,   # Emerging Market Bonds
        'VTEB': 0.02,   # Municipal Bonds
        'VMOT': 0.05,   # Strategic Bonds
        
        # Equities (35%)
        'VTI': 0.20,    # US Total Market
        'VXUS': 0.12,   # International Developed
        'VWO': 0.03,    # Emerging Markets
        
        # Real Estate (7%)
        'VNQ': 0.04,    # US REITs
        'VNQI': 0.03,   # International REITs
        
        # Commodities (3%)
        'IAU': 0.015,   # Gold
        'DJP': 0.01,    # Commodities
        'PDBC': 0.005   # Enhanced Commodities
    }

def download_data(tickers, start='2015-01-01'):
    """Download price data for multiple tickers"""
    data = {}
    
    for ticker in tickers:
        try:
            df = yf.download(ticker, start=start, progress=False)
            if not df.empty:
                if isinstance(df.columns, pd.MultiIndex):
                    # Handle MultiIndex columns
                    if 'Close' in [col[0] for col in df.columns]:
                        data[ticker] = df['Close'].iloc[:, 0] if len(df['Close'].columns) == 1 else df['Close'][ticker]
                else:
                    # Simple columns
                    if 'Close' in df.columns:
                        data[ticker] = df['Close']
                    elif 'Adj Close' in df.columns:
                        data[ticker] = df['Adj Close']
        except Exception as e:
            print(f"Failed to download {ticker}: {e}")
    
    if not data:
        return pd.DataFrame()
    
    return pd.DataFrame(data).dropna(how='all')

def calculate_performance(prices, weights):
    """Calculate portfolio performance given prices and weights"""
    # Get available tickers and normalize weights
    available = [t for t in weights.keys() if t in prices.columns]
    w = np.array([weights[t] for t in available])
    w = w / w.sum()  # Normalize to 100%
    
    # Calculate returns
    returns = prices[available].pct_change().dropna()
    portfolio_returns = (returns * w).sum(axis=1)
    
    # Performance metrics
    cumulative = (1 + portfolio_returns).cumprod()
    annual_return = portfolio_returns.mean() * 252
    annual_vol = portfolio_returns.std() * np.sqrt(252)
    sharpe = annual_return / annual_vol if annual_vol > 0 else 0
    max_dd = (cumulative / cumulative.expanding().max() - 1).min()
    
    return {
        'cumulative': cumulative,
        'annual_return': annual_return,
        'annual_vol': annual_vol,
        'sharpe': sharpe,
        'max_dd': max_dd,
        'weights_used': dict(zip(available, w))
    }

def main():
    # Portfolio definition
    igmp_weights = get_igmp_portfolio()
    benchmarks = ['SPY', 'VT', 'BND', 'ACWI']
    
    # Download data
    all_tickers = list(igmp_weights.keys()) + benchmarks
    print(f"Downloading data for {len(all_tickers)} tickers...")
    data = download_data(all_tickers)
    print(f"Got data for: {list(data.columns)}")
    
    # Calculate IGMP performance
    igmp_perf = calculate_performance(data, igmp_weights)
    
    # Calculate benchmark performance  
    bench_perf = {}
    for ticker in benchmarks:
        if ticker in data.columns:
            single_weight = {ticker: 1.0}
            bench_perf[ticker] = calculate_performance(data, single_weight)
    
    # Results
    print(f"\n=== PERFORMANCE RESULTS ===")
    print(f"IGMP Portfolio:")
    print(f"  Annual Return: {igmp_perf['annual_return']:.1%}")
    print(f"  Volatility: {igmp_perf['annual_vol']:.1%}")
    print(f"  Sharpe Ratio: {igmp_perf['sharpe']:.2f}")
    print(f"  Max Drawdown: {igmp_perf['max_dd']:.1%}")
    
    print(f"\nBenchmarks:")
    for ticker, perf in bench_perf.items():
        print(f"  {ticker}: {perf['annual_return']:.1%} return, {perf['annual_vol']:.1%} vol, {perf['sharpe']:.2f} sharpe")
    
    # Simple plot
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(igmp_perf['cumulative'], label='IGMP', linewidth=2)
    for ticker, perf in bench_perf.items():
        plt.plot(perf['cumulative'], label=ticker, alpha=0.7)
    plt.title('Cumulative Returns')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 2)
    returns = [igmp_perf['annual_return']] + [p['annual_return'] for p in bench_perf.values()]
    vols = [igmp_perf['annual_vol']] + [p['annual_vol'] for p in bench_perf.values()]
    sharpes = [igmp_perf['sharpe']] + [p['sharpe'] for p in bench_perf.values()]
    labels = ['IGMP'] + list(bench_perf.keys())
    
    # Color code by Sharpe ratio
    colors = plt.cm.RdYlGn([s/max(sharpes) for s in sharpes])
    plt.scatter(vols, returns, c=colors, s=100)
    
    for i, label in enumerate(labels):
        plt.annotate(f'{label}\n(S:{sharpes[i]:.2f})', 
                    (vols[i], returns[i]), 
                    xytext=(5, 5), textcoords='offset points', 
                    fontsize=9, ha='left')
    plt.xlabel('Volatility')
    plt.ylabel('Return')
    plt.title('Risk-Return (Sharpe in parentheses)')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 3)
    # Sharpe ratio comparison bar chart
    sharpe_data = {'IGMP': igmp_perf['sharpe']}
    for ticker, perf in bench_perf.items():
        sharpe_data[ticker] = perf['sharpe']
    
    bars = plt.bar(sharpe_data.keys(), sharpe_data.values(), 
                   color=['purple', 'blue', 'green', 'orange', 'red'])
    plt.title('Sharpe Ratio Comparison')
    plt.ylabel('Sharpe Ratio')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for bar, value in zip(bars, sharpe_data.values()):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01, 
                f'{value:.2f}', ha='center', va='bottom')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 4)
    # Weights pie chart
    weights_used = igmp_perf['weights_used']
    categories = {}
    for ticker, weight in weights_used.items():
        if ticker in ['BND', 'BNDX', 'VWOB', 'VTEB', 'VMOT']:
            categories['Bonds'] = categories.get('Bonds', 0) + weight
        elif ticker in ['VTI', 'VXUS', 'VWO']:
            categories['Stocks'] = categories.get('Stocks', 0) + weight
        elif ticker in ['VNQ', 'VNQI']:
            categories['REITs'] = categories.get('REITs', 0) + weight
        else:
            categories['Commodities'] = categories.get('Commodities', 0) + weight
    
    plt.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%')
    plt.title('Portfolio Allocation')
    
    plt.tight_layout()
    plt.savefig('igmp_results.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    print(f"\nChart saved as: igmp_results.png")

if __name__ == "__main__":
    main()