import torch

# Generate input data
input_data = torch.randn(3, 4, 5)

# Call the API
result = input_data.float(memory_format=torch.contiguous_format)