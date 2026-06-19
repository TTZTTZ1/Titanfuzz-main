import torch

# Generate input data
input_tensor = torch.randn(3, 4)

# Call the API
output_tensor = input_tensor.float(memory_format=torch.preserve_format)