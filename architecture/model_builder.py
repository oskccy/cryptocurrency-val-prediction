from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

class ModelBuilder:
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def build_model(self):
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=self.input_shape),
            Dropout(0.2),
            LSTM(50, return_sequences=True),
            Dropout(0.2),
            LSTM(50),
            Dropout(0.2),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model
