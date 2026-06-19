import torch

# Prepare valid input data
input_tensor = torch.tensor([False, True, False])

# Call the API
result = torch.any(input_tensor)

print(result)