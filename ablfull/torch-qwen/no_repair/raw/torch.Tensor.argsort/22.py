import torch

# Prepare valid input data
input_tensor = torch.tensor([4, 3, 2, 1])

# Call the API
sorted_indices = input_tensor.argsort(dim=0, descending=False)

print(sorted_indices)