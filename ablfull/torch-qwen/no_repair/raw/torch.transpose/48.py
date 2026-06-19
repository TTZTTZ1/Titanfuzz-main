import torch

# Prepare valid input data
input_tensor = torch.randn(2, 3)
dim0 = 0
dim1 = 1

# Call the API
result = torch.transpose(input_tensor, dim0, dim1)
print(result)