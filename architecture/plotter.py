import matplotlib.pyplot as plt


class Plotter:
    @staticmethod
    def plot_results(crypto, actual_prices, prediction_prices):
        plt.figure()
        plt.title(f'{crypto} Price Prediction')
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.plot([], [], color='black', label='Actual Prices')
        plt.plot([], [], color='green', label='Predicted Prices')
        plt.legend(loc='upper right')
        max_points = len(actual_prices)

        for i in range(5, max_points):
            plt.clf()

            plt.plot([], [], color='black', label='Actual Prices')
            plt.plot([], [], color='green', label='Predicted Prices')
            plt.legend(loc='upper right')

            plt.title(f'{crypto} Price Prediction')
            plt.xlabel('Time')
            plt.ylabel('Price')

            if i >= 5:
                plt.plot(range(
                    i - 5 + 1), actual_prices[:i - 5 + 1], color='black', label='Actual Prices' if i == 5 else "")
            plt.plot(range(i + 1), prediction_prices[:i + 1, 0],
                     color='green', label='Predicted Prices' if i == 0 else "")

            percent_error = abs(
                (actual_prices[i] - prediction_prices[i, 0]) / actual_prices[i]) * 100

            plt.text(0.05, 0.95, f'Percent Error: {percent_error:.2f}%',
                     horizontalalignment='left',
                     verticalalignment='top',
                     transform=plt.gca().transAxes,
                     bbox=dict(facecolor='white', alpha=0.5))

            plt.pause(1)

        plt.show()
