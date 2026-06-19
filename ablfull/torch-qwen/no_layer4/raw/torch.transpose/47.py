import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 2], [3, 4]])
dim0 = 0
dim1 = 1

# Call the API
output_tensor = torch.transpose(input_tensor, dim0, dim1)
print(output_tensor)