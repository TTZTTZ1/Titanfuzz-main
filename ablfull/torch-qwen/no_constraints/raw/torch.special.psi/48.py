import torch

# Prepare valid input data
x = torch.tensor([1.0], dtype=torch.float32)

# Call the API
result = torch.special.psi(x)
print(result)