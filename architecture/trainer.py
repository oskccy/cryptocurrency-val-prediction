import numpy as np

class Trainer:
    def __init__(self, model, data_depth=60):
        self.model = model
        self.data_depth = data_depth

    def create_training_data(self, scaled_data):
        x_train, y_train = [], []
        for x in range(self.data_depth, len(scaled_data)):
            x_train.append(scaled_data[x-self.data_depth:x, 0])
            y_train.append(scaled_data[x, 0])
        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        return x_train, y_train

    def train(self, x_train, y_train, epochs=25, batch_size=32):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
