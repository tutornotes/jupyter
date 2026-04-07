import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
x_train_flat = x_train.reshape(-1, 28*28)
x_test_flat = x_test.reshape(-1, 28*28)
def build_ffn():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(784,)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model
batch_size  = 128
epochs = 10
loss_fn = 'sparse_categorical_crossentropy'
metrics = ['accuracy']
optimizers = {
'SGD': tf.keras.optimizers.SGD(learning_rate=0.01),
'RMSProp': tf.keras.optimizers.RMSprop(learning_rate=0.001),
'Adam': tf.keras.optimizers.Adam(learning_rate=0.001)
}
histories = {}
for name, opt in optimizers.items():
    print(f"\n--- Training with optimizer: {name} ---")
    model = build_ffn()
    model.compile(optimizer=opt, loss=loss_fn, metrics=metrics)
    history = model.fit(
        x_train_flat, y_train,
        validation_split=0.1,
        epochs=epochs,
        batch_size=batch_size,
        verbose=2
    )
    test_loss, test_acc = model.evaluate(x_test_flat, y_test,
                                          verbose=0)
    print(f"{name} test accuracy: {test_acc:.4f}, test loss: {test_loss:.4f}")
    histories[name] = {
        'history': history.history,
        'test_loss': test_loss,
        'test_acc': test_acc
    }
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
for name, data in histories.items():
    plt.plot(data['history']['loss'], label=f"{name} train loss")
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.subplot(1,2,2)
for name, data in histories.items():
    plt.plot(data['history']['val_accuracy'], label=f"{name} val acc")
plt.title("Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.show()
print("\nFinal test accuracies:")
for name, data in histories.items():
    print(f"{name}: accuracy={data['test_acc']:.4f}, loss={data['test_loss']:.4f}")
