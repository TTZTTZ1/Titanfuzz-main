import torch
from torch.nn import Sequential, Linear

# Task 2: Generate input data
model = Sequential(Linear(5, 10), Linear(10, 1))
input_data = torch.randn(3, 5)

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_data, use_reentrant=True)