import torch

# Prepare valid input data
tensor = torch.tensor([3, 1, 4, 1, 5])

# Call the API
sorted_indices = tensor.argsort(dim=0)

print(sorted_indices)