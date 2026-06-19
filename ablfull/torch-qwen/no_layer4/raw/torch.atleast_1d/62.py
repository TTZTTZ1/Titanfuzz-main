import torch

# Input data preparation
input_data = torch.tensor([1.0, 2.0, 3.0])

# Calling the API
result = torch.atleast_1d(input_data)
print(result)