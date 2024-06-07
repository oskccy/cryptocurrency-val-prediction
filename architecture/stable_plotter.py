import matplotlib.pyplot as plt
import numpy as np
# safetesting


class Plotter:
    @staticmethod
    def plot_results(crypto, actual_prices, prediction_prices):
        plt.figure()
        plt.title(f'{crypto} Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Price')

        for actual, predicted in zip(actual_prices, prediction_prices):
            actual_index = np.where(actual_prices == actual)[0][0] + 1
            plt.plot(range(len(actual_prices[:actual_index])),
                     actual_prices[:actual_index], color='black', label='Actual Prices')
            plt.plot(range(len(prediction_prices[:actual_index])),
                     prediction_prices[:actual_index, 0], color='green', label='Predicted Prices')
            plt.pause(1)

        plt.legend(loc='upper right')
        plt.show()
