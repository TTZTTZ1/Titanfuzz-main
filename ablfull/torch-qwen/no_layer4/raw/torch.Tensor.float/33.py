import torch

# Generate input data
data = torch.randn(3, 4)

# Call the API
result = data.float(memory_format=torch.channels_last)