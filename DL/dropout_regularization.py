# Step 1: Import Required Libraries
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# a) Load dataset and preprocess
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 28*28) / 255.0
x_test = x_test.reshape(10000, 28*28) / 255.0

# b) Baseline model (No Regularization)
model_no_reg = models.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model_no_reg.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_no_reg = model_no_reg.fit(
    x_train, y_train,
    epochs=20,
    validation_data=(x_test, y_test)
)

# c) Model with Dropout Regularization
model_dropout = models.Sequential([
    layers.Dense(256, activation='relu', input_shape=(784,)),
    layers.Dropout(0.5),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model_dropout.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_dropout = model_dropout.fit(
    x_train, y_train,
    epochs=20,
    validation_data=(x_test, y_test)
)

# d) Compare Training vs Validation Performance

# Accuracy comparison
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(history_no_reg.history['accuracy'], label='Train No Reg')
plt.plot(history_no_reg.history['val_accuracy'], label='Val No Reg')

plt.plot(history_dropout.history['accuracy'], label='Train Dropout')
plt.plot(history_dropout.history['val_accuracy'], label='Val Dropout')

plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Loss comparison
plt.subplot(1,2,2)
plt.plot(history_no_reg.history['loss'], label='Train No Reg')
plt.plot(history_no_reg.history['val_loss'], label='Val No Reg')

plt.plot(history_dropout.history['loss'], label='Train Dropout')
plt.plot(history_dropout.history['val_loss'], label='Val Dropout')

plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()