import torch

# Prepare input data
input_tensor = torch.tensor([[10, 5, 3], [8, 2, 9]])

# Call the API
sorted_indices = input_tensor.argsort(dim=1, descending=True)

print(sorted_indices)