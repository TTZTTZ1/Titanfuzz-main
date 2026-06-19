import torch

# Task 2: Generate input data
data = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Task 3: Call the API
dataset = torch.utils.data.Dataset(data)