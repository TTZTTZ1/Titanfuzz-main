import torch

# Generate input data
input_data = torch.randn(4, 4)

# Call the API
result = input_data.float(memory_format=torch.channels_last)