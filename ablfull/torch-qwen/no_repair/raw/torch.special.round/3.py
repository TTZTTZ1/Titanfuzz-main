import torch

# Prepare valid input data
input_tensor = torch.tensor([1.5, -2.3, 0.8], dtype=torch.float)

# Call the API with the prepared input data
result = torch.special.round(input_tensor)
print(result)