import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Define indices to select
indices = torch.tensor([0])

# Use torch.index_select to select rows from the tensor
selected_tensor = torch.index_select(tensor, 0, indices)

print(selected_tensor)