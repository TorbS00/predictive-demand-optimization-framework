from src.optimization import optimize_stock


def sensitivity_analysis(prices, demands, stock_capacity):
    for capacity in range(100, stock_capacity+1, 100):
        result = optimize_stock(prices, demands, capacity)
        print(f'For capacity {capacity}: {result}')