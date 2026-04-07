# Step 1: Import Required Libraries
import tensorflow as tf
from tensorflow.keras import layers, models, regularizers
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = mnist.load_data()


x_train = x_train.reshape(60000, 28*28) / 255.0
x_test = x_test.reshape(10000, 28*28) / 255.0


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


plt.plot(history_no_reg.history['val_accuracy'], label='No Reg')
plt.plot(history_l2.history['val_accuracy'], label='L2')
plt.plot(history_dropout.history['val_accuracy'], label='Dropout')
plt.title('Validation Accuracy Comparison')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

