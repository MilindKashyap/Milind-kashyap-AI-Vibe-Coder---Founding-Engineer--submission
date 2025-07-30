import pandas as pd
import numpy as np
import pickle
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm

def load_data(file_path='MultiTimeline.csv'):
    """
    Load and preprocess the dataset
    """
    df = pd.read_csv(file_path, index_col='Month', parse_dates=True)
    df.index = pd.DatetimeIndex(df.index).to_period('M')
    return df

def train_test_split(data, column='Premier League', split_index=150):
    """
    Split the dataset into training and testing sets
    """
    train = data[0:split_index]
    test = data[split_index:]
    return train, test

def train_football_arima(train_series, order=(2, 1, 4)):
    """
    Train the ARIMA model for football
    """
    model = ARIMA(train_series, order=order)
    results = model.fit()
    return results

def predict_future(model, steps=6):
    """
    Make future predictions using the trained model
    """
    forecast = model.forecast(steps=steps)
    return forecast

# Plot function removed for web deployment - not needed for API

def save_model(model, filename='football_arima_model.pkl'):
    """
    Save the trained model to a file
    """
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model(filename='football_arima_model.pkl'):
    """
    Load a trained model from a file
    """
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    df = load_data()
    train, test = train_test_split(df, 'Premier League')
    model = train_football_arima(train['Premier League'])
    predictions = predict_future(model, steps=6)
    
    save_model(model)

if __name__ == "__main__":
    main() 