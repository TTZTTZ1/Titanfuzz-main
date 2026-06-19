import torch

# Prepare valid input data
input_tensor = torch.tensor([1.5, -0.3, 4.7])

# Call the API
result = torch.special.round(input_tensor)

print(result)