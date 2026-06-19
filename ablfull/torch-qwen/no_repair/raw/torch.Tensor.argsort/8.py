import torch

# Prepare valid input data
tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6])

# Call the API
result = tensor.argsort(dim=0, descending=False)
print(result)