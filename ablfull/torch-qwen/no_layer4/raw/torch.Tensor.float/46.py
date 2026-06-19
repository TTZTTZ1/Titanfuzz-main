import torch

# Generate input data
input_data = torch.randn(3, 3)

# Call the API
result = input_data.float(memory_format=torch.preserve_format)