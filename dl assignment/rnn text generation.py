import tensorflow as tf
import numpy as np

text = "Deep learning models learn patterns from sequential data efficiently."
chars = sorted(set(text))

char_to_idx = {c:i for i,c in enumerate(chars)}
idx_to_char = dict(enumerate(chars))

seq_len = 10
X, y = [], []

for i in range(len(text) - seq_len):
    X.append([char_to_idx[c] for c in text[i:i+seq_len]])
    y.append(char_to_idx[text[i+seq_len]])

X = np.array(X)
y = np.array(y)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(len(chars), 16, input_length=seq_len),
    tf.keras.layers.SimpleRNN(64),
    tf.keras.layers.Dense(len(chars), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
model.fit(X, y, epochs=50)
