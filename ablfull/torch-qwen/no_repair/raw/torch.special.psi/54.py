import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5, 1.0, 1.5], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_tensor)
print(result)