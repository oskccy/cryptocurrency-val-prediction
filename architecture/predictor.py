import numpy as np

class Predictor:
    def __init__(self, model, scaler, data_depth=60):
        self.model = model
        self.scaler = scaler
        self.data_depth = data_depth

    def create_test_data(self, total_dataset, test_data):
        model_inputs = total_dataset[len(total_dataset) - len(test_data) - self.data_depth:].values
        model_inputs = model_inputs.reshape(-1, 1)
        model_inputs = self.scaler.fit_transform(model_inputs)

        x_test = []
        for x in range(self.data_depth, len(model_inputs)):
            x_test.append(model_inputs[x-self.data_depth:x, 0])
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        return x_test

    def predict(self, x_test):
        prediction_prices = self.model.predict(x_test)
        prediction_prices = self.scaler.inverse_transform(prediction_prices)
        return prediction_prices
