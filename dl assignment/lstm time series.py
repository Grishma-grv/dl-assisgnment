import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("daily_temperature.csv")
values = data.iloc[:,1].values.reshape(-1,1)

scaler = MinMaxScaler()
values = scaler.fit_transform(values)

X, y = [], []
for i in range(10, len(values)):
    X.append(values[i-10:i])
    y.append(values[i])

X, y = tf.convert_to_tensor(X), tf.convert_to_tensor(y)

model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=30, batch_size=16)
