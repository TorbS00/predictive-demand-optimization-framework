from src.data_processing import load_data, clean_data

def test_load_data():
    df = load_data('data/historical_data.csv')
    assert not df.empty

def test_clean_data():
    df = load_data('data/historical_data.csv')
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0