import torch

# Generate input data
input_tensor = torch.tensor([4, 2, 5, 1])

# Call the API
sorted_indices = input_tensor.argsort(dim=0)

print(sorted_indices)