import torch

# Prepare input data
input_tensor = torch.tensor([4, 2, 5, 1])

# Call the API
sorted_indices = input_tensor.argsort(dim=0, descending=False)

print(sorted_indices)