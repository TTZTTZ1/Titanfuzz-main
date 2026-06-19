import torch

# Generate input data
data = torch.tensor([3, 1, 4, 1, 5, 9, 2])

# Call the API
sorted_indices = data.argsort()

print(sorted_indices)