from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def create_sequences(values, time_steps=100):
    output = []
    for i in range(len(values) - time_steps + 1):
        output.append(values[i : (i + time_steps)])
    return np.stack(output).reshape(len(output),time_steps,1)

def model():
  model = keras.Sequential(
    [
        layers.Input(shape=(x_train.shape[1], x_train.shape[2])),
        layers.Conv1D(
            filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Dropout(rate=0.2),
        layers.Conv1D(
            filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Conv1DTranspose(
            filters=16, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Dropout(rate=0.2),
        layers.Conv1DTranspose(
            filters=32, kernel_size=7, padding="same", strides=2, activation="relu"
        ),
        layers.Conv1DTranspose(filters=1, kernel_size=7, padding="same"),
    ]
  )
  model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001), loss="mse")
  return(model)

def save_and_train_model(training_set,model,model_path):
  model_checkpoint_callback = keras.callbacks.ModelCheckpoint(
    filepath=model_path+'/checkpoints',
    monitor='val_loss',
    mode='min')
  
  model.fit(
    x_train,
    x_train,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[
        keras.callbacks.EarlyStopping(monitor="val_loss", patience=2, mode="min"),
        model_checkpoint_callback
    ],
  )
  model.save(model_path)

def test_model(number_subsets):
  for k in range(number_subsets):
    input = anomaly[100*k:100*k +100].values.reshape(100,1)
    prediction = model.predict(input)
    train_mae_loss = np.mean(np.abs(prediction[:,-1] - input), axis=0)
    print(train_mae_loss)
