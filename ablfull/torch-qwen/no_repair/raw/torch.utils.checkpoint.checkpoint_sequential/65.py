import torch
from torch.nn import Sequential, Linear

# Task 2: Generate input data
functions = Sequential(
    Linear(5, 10),
    Linear(10, 15),
    Linear(15, 20)
)
segments = 2
input_tensor = torch.randn(1, 5)

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)