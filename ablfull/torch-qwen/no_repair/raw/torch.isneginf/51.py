import torch

# Prepare valid input data
input_tensor = torch.tensor(-float('inf'))

# Call the API
result = torch.isneginf(input_tensor)

print(result)