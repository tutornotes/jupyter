import kagglehub
import os

# Load dataset
path = kagglehub.dataset_download("chetankv/dogs-cats-images")
print("Path to dataset files:", path)

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

# Faster preprocessing (smaller images)
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    directory=path,
    target_size=(128, 128),   # reduced size (faster)
    batch_size=16,            # smaller batch (faster)
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    directory=path,
    target_size=(128, 128),
    batch_size=16,
    class_mode='binary',
    subset='validation'
)

# Faster model (no pretrained weights download)
base_model = VGG16(
    weights=None,   # removed heavy download
    include_top=False,
    input_shape=(128, 128, 3)
)

base_model.trainable = False

model = Sequential([
    base_model,
    Flatten(),
    Dense(64, activation='relu'),   # smaller layer
    Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train quickly
history = model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=1   # reduced epochs
)

# Evaluate
loss, acc = model.evaluate(validation_generator)
print("Validation Accuracy:", acc)

# Plot
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()

plt.show()