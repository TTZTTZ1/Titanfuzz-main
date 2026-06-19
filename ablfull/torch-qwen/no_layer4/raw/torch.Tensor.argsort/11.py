import torch

# Generate input data
input_tensor = torch.tensor([[1, 0, 2], [3, 4, 5]])

# Call the API
sorted_indices = input_tensor.argsort(dim=1)

print(sorted_indices)