import torch
from torch.nn import Sequential, Linear

# Step 2: Generate input data
input_tensor = torch.randn(10)
functions = Sequential(Linear(10, 5), Linear(5, 2))
segments = 2

# Step 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)