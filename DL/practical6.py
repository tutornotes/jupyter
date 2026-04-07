
!pip install kagglehub

import kagglehub

path = kagglehub.dataset_download("chetankv/dogs-cats-images")
print("Path to dataset files:", path)


import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
train_generator = train_datagen.flow_from_directory(
directory=path,
target_size=(224, 224),
batch_size=32,
class_mode='binary',
subset='training'
)
validation_generator = train_datagen.flow_from_directory(
directory=path,
target_size=(224, 224),
batch_size=32,
class_mode='binary',
subset='validation'
)

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=3
)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=3,
    steps_per_epoch=20,
    validation_steps=10
)

model.evaluate(validation_generator)

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np


model = MobileNetV2(weights='imagenet')


img_path = r'/content/test.jpg'

img = image.load_img(img_path, target_size=(224, 224))


x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


preds = model.predict(x)


print('Predicted:', decode_predictions(preds, top=3)[0])

