import datetime as dt
import pandas as pd

from architecture.data_loader import DataLoader
from architecture.model_builder import ModelBuilder
from architecture.trainer import Trainer
from architecture.predictor import Predictor
from architecture.plotter import Plotter


def get_user_inputs():
    crypto = input("Enter the crypto ticker: ")
    against = input("Enter the currency to compare against: ")
    return crypto, against


if __name__ == "__main__":
    crypto, against = get_user_inputs()
    if not crypto or not against:
        print("No valid inputs provided. Exiting.")
    else:
        start = dt.datetime(2016, 1, 1)
        end = dt.datetime.now()
        data_depth = 60

        print("Starting Machine Learning Processes")
        data_loader = DataLoader(crypto, against, start, end)
        price_data = data_loader.load_data()
        scaled_data, scaler = data_loader.preprocess_data(price_data)

        model_builder = ModelBuilder(input_shape=(data_depth, 1))
        model = model_builder.build_model()

        trainer = Trainer(model, data_depth)
        x_train, y_train = trainer.create_training_data(scaled_data)
        trainer.train(x_train, y_train)

        test_start = dt.datetime(2020, 1, 1)
        test_end = dt.datetime.now()
        test_data = data_loader.currency_pair.history(
            start=test_start, end=test_end, interval="1d")
        actual_prices = test_data['Close'].values
        total_dataset = pd.concat(
            (price_data['Close'], test_data['Close']), axis=0)

        predictor = Predictor(model, scaler, data_depth)
        x_test = predictor.create_test_data(total_dataset, test_data)
        prediction_prices = predictor.predict(x_test)

        Plotter.plot_results(crypto, actual_prices, prediction_prices)
