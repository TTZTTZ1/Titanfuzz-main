import torch

# Task 2: Generate input data
functions = torch.nn.Sequential(torch.nn.Linear(10, 5), torch.nn.ReLU(), torch.nn.Linear(5, 1))
segments = 2
input_tensor = torch.randn(1, 10)

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments, input_tensor)