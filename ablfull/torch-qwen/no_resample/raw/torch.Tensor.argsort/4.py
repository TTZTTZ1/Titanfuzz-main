import torch

# Generate input data
tensor = torch.tensor([4, 1, 3, 2])

# Call the API
sorted_indices = tensor.argsort(dim=0, descending=False)

print(sorted_indices)