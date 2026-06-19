import torch

# Generate input data
tensor = torch.tensor([4, 3, 1, 2])

# Call the API
sorted_indices = tensor.argsort(dim=0)

print(sorted_indices)