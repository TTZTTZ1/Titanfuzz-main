import torch

# Prepare valid input data
input_tensor = torch.tensor([[False, True], [False, False]])

# Call the API torch.any
result = torch.any(input_tensor, dim=1)
print(result)