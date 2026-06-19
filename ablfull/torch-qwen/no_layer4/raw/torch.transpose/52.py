import torch

# Prepare valid input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
dim0, dim1 = 0, 1

# Call the API
result = torch.transpose(input_tensor, dim0, dim1)