import torch

# Prepare valid input data
input_tensor = torch.tensor([3, 1, 4, 1, 5])

# Call the API
sorted_indices = input_tensor.argsort(dim=0, descending=False)

print(sorted_indices)