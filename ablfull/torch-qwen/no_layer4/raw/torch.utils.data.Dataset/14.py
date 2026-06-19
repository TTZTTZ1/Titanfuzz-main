import torch

# Generate input data
data = [torch.randn(3, 4) for _ in range(5)]  # List of 5 tensors

# Call the API
dataset = torch.utils.data.Dataset(data)