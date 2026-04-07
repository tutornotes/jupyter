
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np


(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()


print(x_train.shape)
print(y_train.shape)


x_train = x_train / 255.0
x_test = x_test / 255.0


class_names = ['airplane','automobile','bird','cat','deer',
'dog','frog','horse','ship','truck']


plt.figure(figsize=(8,8))
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(x_train[i])
    plt.title(class_names[y_train[i][0]])
    plt.axis('off')
plt.show()


model = models.Sequential()

model.add(layers.Conv2D(32, (3,3), activation='relu',
input_shape=(32,32,3))) 
model.add(layers.MaxPooling2D((2,2))) 

model.add(layers.Conv2D(64, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Flatten())

model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy',
metrics=['accuracy'])


history = model.fit(x_train, y_train,
epochs=10,
validation_data=(x_test, y_test))


test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)


predictions = model.predict(x_test)

index = 5
predicted_class = np.argmax(predictions[index])
print("Predicted:", class_names[predicted_class])
print("Actual:", class_names[y_test[index][0]])

