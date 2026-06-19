import torch

# Prepare valid input data
input_tensor = torch.tensor([[1, 3, 2]])

# Call the API
sorted_indices = input_tensor.argsort(dim=1)

print(sorted_indices)