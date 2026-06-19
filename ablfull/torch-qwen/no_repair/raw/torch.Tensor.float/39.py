import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4)

# Call the API
output_tensor = input_tensor.float(memory_format=torch.contiguous_format)