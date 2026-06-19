import torch
import torch.nn as nn
from torch.nn.utils import prune
model = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
name = 'weight'
amount = 0.5
dim = 1
prune.random_structured(model, name, amount, dim)