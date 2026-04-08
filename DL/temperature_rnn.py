import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Given temperature dataset
data = np.array([30, 31, 32, 33, 34, 35, 36, 35, 34, 33,
                 32, 31, 30, 29, 28, 27, 28, 29, 30, 31])

# a) Prepare sequential dataset (4 → 1)
X = []
y = []

for i in range(len(data) - 4):
    X.append(data[i:i+4])
    y.append(data[i+4])

X = np.array(X)
y = np.array(y)

# Reshape for RNN
X = X.reshape((X.shape[0], 4, 1))

# b) Build RNN model
model = Sequential()
model.add(SimpleRNN(8, input_shape=(4, 1)))
model.add(Dense(1))

# c) Compile & train
model.compile(optimizer='adam', loss='mse')

history = model.fit(X, y, epochs=200, verbose=0)

# d) Predict values
predictions = model.predict(X)

# Predict future value using last 4 temperatures
last_input = data[-4:].reshape(1, 4, 1)
future_pred = model.predict(last_input)

print("Last 4 temperatures:", data[-4:])
print("Predicted next temperature:", future_pred[0][0])

# e) Compare predicted vs actual
plt.plot(y, label='Actual')
plt.plot(predictions, label='Predicted')
plt.title('Actual vs Predicted Temperature')
plt.xlabel('Time Step')
plt.ylabel('Temperature')
plt.legend()
plt.show()