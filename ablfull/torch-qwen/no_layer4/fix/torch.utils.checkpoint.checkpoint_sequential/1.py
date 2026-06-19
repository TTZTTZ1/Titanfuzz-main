import torch
from torch.nn import Sequential, Linear
functions = Sequential(Linear(5, 10), Linear(10, 1))
segments = 1
input_data = torch.randn(3, 5)
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_data, use_reentrant=True)