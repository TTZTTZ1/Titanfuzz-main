import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4, 5)

# Call the API with default parameters
output_tensor = input_tensor.float(memory_format=torch.preserve_format)