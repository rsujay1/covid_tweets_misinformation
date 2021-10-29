import matplotlib.pyplot as plt
import pandas as pd
import torch

from data_building import destination_folder
from save_load import load_metrics

train_loss_list, valid_loss_list, global_steps_list = load_metrics(destination_folder + '/metrics.pt')
plt.plot(global_steps_list, train_loss_list, label='Train')
plt.plot(global_steps_list, valid_loss_list, label='Valid')
plt.xlabel('Steps')
plt.ylabel('Loss')
plt.legend()
plt.show()