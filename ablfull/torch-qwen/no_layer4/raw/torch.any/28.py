import torch

# Prepare valid input data
input_tensor = torch.tensor([[0, 0], [0, 1]])

# Call the API
result = torch.any(input_tensor)

print(result)