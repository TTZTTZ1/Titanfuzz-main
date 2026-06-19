import torch

# Prepare valid input data
input_tensor = torch.tensor([-float('inf'), -1.0, 0.0, 1.0])

# Call the API
result = torch.isneginf(input_tensor)

print(result)