import torch

# Task 2: Generate input data
data = torch.randn(4, 4)

# Task 3: Call the API torch.Tensor.float
result = data.float(memory_format=torch.channels_last)