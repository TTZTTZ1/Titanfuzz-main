import torch

# Generate input data
input_data = torch.tensor([3, 1, 4, 1, 5, 9], dtype=torch.int)

# Call the API
sorted_indices = torch.argsort(input_data)

print(sorted_indices)