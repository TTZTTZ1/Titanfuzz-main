import torch

# Prepare valid input data
input_tensor = torch.tensor([[True, False], [False, True]])

# Call the API
result = torch.any(input_tensor)

print(result)