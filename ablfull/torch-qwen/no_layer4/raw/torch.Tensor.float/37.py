import torch

# Generate input data
input_data = torch.randn(4, 4)

# Call the API
output_data = input_data.float(memory_format=torch.preserve_format)