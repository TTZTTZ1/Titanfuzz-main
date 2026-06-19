import torch

# Prepare input data
input_tensor = torch.tensor([[1, 0, 2], [4, 5, 6]])

# Call the API
sorted_indices = input_tensor.argsort(dim=1)

print(sorted_indices)