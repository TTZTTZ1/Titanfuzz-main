import torch

# Task 2: Generate input data
data = [torch.randn(3) for _ in range(4)]  # List of 4 tensors of shape (3,)

# Task 3: Call the API torch.utils.data.Dataset
dataset = torch.utils.data.Dataset(data)