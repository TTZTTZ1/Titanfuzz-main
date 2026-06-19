import torch

# Generate input data
input_tensor = torch.randn(3, 4)

# Call the API
result = input_tensor.float(memory_format=torch.contiguous_format)