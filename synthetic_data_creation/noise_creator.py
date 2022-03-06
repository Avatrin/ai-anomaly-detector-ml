import numpy as np
import pandas as pd

def create_noise(len):
  randoms = np.zeros(len)
  rand_value = 0

  for i in range(len):
    rand_value +=(np.random.random()-0.5)/1000
    randoms[i] = rand_value
  return(randoms)

def save_noise(noise,path):
  np.savetxt(path, noise, delimiter=",")

if __name__ == "__main__":
  import matplotlib.pyplot as plt
  randoms = create_noise(6000)
  plt.figure(figsize=(8,8))
  plt.plot(randoms)
