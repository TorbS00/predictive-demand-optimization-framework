from src.data_processing import load_data, clean_data
from src.ml_forecasting import forecast_demand
from src.optimization import optimize_stock
from src.visualization import plot_demand_trends

df = load_data('data/historical_data.csv')
cleaned_df = clean_data(df)

model, error = forecast_demand(cleaned_df, features=['Price'], target='Demand')

prices = {'Product_A': 10, 'Product_B': 15}
predicted_demand = {'Product_A': 100, 'Product_B': 150}
optimal_stock = optimize_stock(prices, predicted_demand, stock_capacity=200)

plot_demand_trends(df, 'Demand', save_as_pdf=True)

# Final output
print(f'Optimal stock levels: {optimal_stock}')