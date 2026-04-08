import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Given rainfall dataset
data = np.array([2.1, 2.5, 3.0, 3.4, 3.8, 4.0, 4.5, 5.1, 5.8, 6.2,
                 6.5, 6.9, 7.3, 7.8, 8.2, 8.6, 9.0, 8.5, 8.0, 7.6])

# a) Prepare sequential dataset (4 → 1)
X = []
y = []

for i in range(len(data) - 4):
    X.append(data[i:i+4])
    y.append(data[i+4])

X = np.array(X)
y = np.array(y)

# Reshape for RNN [samples, timesteps, features]
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

# Predict future value using last 4 values
last_input = data[-4:].reshape(1, 4, 1)
future_pred = model.predict(last_input)

print("Last 4 values:", data[-4:])
print("Predicted next rainfall:", future_pred[0][0])

# e) Compare predicted vs actual
plt.plot(y, label='Actual')
plt.plot(predictions, label='Predicted')
plt.title('Actual vs Predicted Rainfall')
plt.xlabel('Time Step')
plt.ylabel('Rainfall')
plt.legend()
plt.show()