# Step 1: Import Required Libraries
import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
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

# c) Model with L2 Regularization
model_l2 = models.Sequential([
    layers.Dense(256, activation='relu',
                 kernel_regularizer=regularizers.l2(0.001),
                 input_shape=(784,)),
    layers.Dense(256, activation='relu',
                 kernel_regularizer=regularizers.l2(0.001)),
    layers.Dense(10, activation='softmax')
])

model_l2.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_l2 = model_l2.fit(
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

plt.plot(history_l2.history['accuracy'], label='Train L2')
plt.plot(history_l2.history['val_accuracy'], label='Val L2')

plt.title('Training vs Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Loss comparison
plt.subplot(1,2,2)
plt.plot(history_no_reg.history['loss'], label='Train No Reg')
plt.plot(history_no_reg.history['val_loss'], label='Val No Reg')

plt.plot(history_l2.history['loss'], label='Train L2')
plt.plot(history_l2.history['val_loss'], label='Val L2')

plt.title('Training vs Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()
plt.show()