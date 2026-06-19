import torch

# Prepare valid input data
input_tensor = torch.tensor([4, 2, 5, 1])

# Call the API
result = input_tensor.cummin(dim=0)

print(result)