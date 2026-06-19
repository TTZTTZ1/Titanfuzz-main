import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4)

# Call the API
result_tensor = input_tensor.double(memory_format=torch.preserve_format)