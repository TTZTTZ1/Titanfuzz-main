import torch

# Prepare valid input data
input_tensor = torch.randn(4, 5)

# Call the API
result = torch.transpose(input_tensor, dim0=0, dim1=1)