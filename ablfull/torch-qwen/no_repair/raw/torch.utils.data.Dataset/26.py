import torch

# Generate input data
data = [torch.randn(3) for _ in range(5)]

# Call the API
dataset = torch.utils.data.Dataset(data)