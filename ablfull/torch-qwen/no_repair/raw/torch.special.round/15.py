import torch

# Prepare valid input data
input_tensor = torch.tensor([1.5, -0.4, 2.8], dtype=torch.float)

# Call the API
result = torch.special.round(input_tensor)
print(result)