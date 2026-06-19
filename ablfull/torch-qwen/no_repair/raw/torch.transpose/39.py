import torch

# Prepare valid input data
a = torch.randn(4, 5)

# Call the API
result = torch.transpose(a, 0, 1)
print(result)