
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np


(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()


print(x_train.shape)
print(y_train.shape)


x_train = x_train / 255.0
x_test = x_test / 255.0


plt.figure(figsize=(6,6))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(y_train[i])
    plt.axis('off')
plt.show()


model = models.Sequential()

model.add(layers.Flatten(input_shape=(28, 28)))

model.add(layers.Dense(128, activation='relu'))

model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


history = model.fit(x_train, y_train,
                    epochs=20,
                    validation_data=(x_test, y_test))


test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)


predictions = model.predict(x_test)
index = 7
predicted_digit = np.argmax(predictions[index])
print("Predicted:", predicted_digit)
print("Actual:", y_test[index])


plt.imshow(x_test[index], cmap='gray')
plt.title(f"Predicted: {predicted_digit}")
plt.axis('off')
plt.show()

