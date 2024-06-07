import yfinance as yf
from sklearn.preprocessing import MinMaxScaler


class DataLoader:
    def __init__(self, crypto, against, start, end):

        self.ticker = f'{crypto}-{against}'
        self.start = start
        self.end = end
        # api call
        self.currency_pair = yf.Ticker(self.ticker)

    def load_data(self):
        price_data = self.currency_pair.history(
            start=self.start, end=self.end, interval="1d")
        return price_data

    def preprocess_data(self, data, column='Close'):
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(data[column].values.reshape(-1, 1))
        return scaled_data, scaler
