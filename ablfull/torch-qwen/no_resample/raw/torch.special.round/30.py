import torch

# Prepare valid input data
input_tensor = torch.tensor([1.5, -0.7, 3.2, -4.8])

# Call the API
result = torch.special.round(input_tensor)

print(result)