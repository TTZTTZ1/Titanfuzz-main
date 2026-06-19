import torch

# Generate input data
input_tensor = torch.tensor([[10, 50, 30], [60, 20, 40]])

# Call the API
sorted_indices = input_tensor.argsort(dim=1, descending=True)

print(sorted_indices)