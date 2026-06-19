import torch

# Generate input data
input_data = torch.randn(3, 4)

# Call the API
output_data = input_data.float(memory_format=torch.contiguous_format)