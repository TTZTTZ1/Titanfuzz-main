import torch

# Generate input data
input_tensor = torch.tensor([4, 3, 1, 2])

# Call the API
sorted_indices = input_tensor.argsort(dim=0)

print(sorted_indices)