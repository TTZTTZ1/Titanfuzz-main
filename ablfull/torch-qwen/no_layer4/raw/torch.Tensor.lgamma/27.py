import torch

# Prepare valid input data
x = torch.tensor([1.0, 2.5])

# Call the API
result = x.lgamma()
print(result)