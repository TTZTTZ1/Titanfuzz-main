import torch

# Generate input data
input_tensor = torch.tensor([4, 2, 5, 1, 3])

# Call the API
sorted_indices = input_tensor.argsort()

print(sorted_indices)