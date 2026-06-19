import torch

# Prepare valid input data
input_tensor = torch.tensor([4, 1, 2, 3])

# Call the API
sorted_indices = input_tensor.argsort(dim=0)

print(sorted_indices)