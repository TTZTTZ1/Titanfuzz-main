import torch

# Prepare valid input data
input_data = torch.randn(3, 4)

# Call the API
output_tensor = input_data.float(memory_format=torch.contiguous_format)