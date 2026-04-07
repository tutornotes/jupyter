import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
X = np.array([
[10, 12, 13, 15],
[12, 13, 15, 16],
[13, 15, 16, 18],
[15, 16, 18, 20]
])
y = np.array([16, 18, 20, 22])
X = X.reshape(X.shape[0], 4, 1)
model = Sequential()
model.add(SimpleRNN(8, input_shape=(4, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=200, verbose=0)
test = np.array([[16, 18, 20, 22]]).reshape(1, 4, 1)
prediction = model.predict(test)
print("Rainfall of previous 4 days:", test.flatten())
print("Predicted rainfall for next day:", prediction[0][0])