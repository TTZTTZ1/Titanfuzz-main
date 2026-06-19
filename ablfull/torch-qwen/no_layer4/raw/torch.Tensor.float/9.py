import torch

# Generate input data
input_data = torch.randn(3, 4)

# Call the API
output = input_data.float(memory_format=torch.preserve_format)