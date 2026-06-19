import torch

# Generate input data
data = torch.randn(4, 3, 64, 64)

# Call the API
result = data.float(memory_format=torch.channels_last)