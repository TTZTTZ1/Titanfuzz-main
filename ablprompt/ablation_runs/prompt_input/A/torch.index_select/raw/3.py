import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4], [5, 6]])

# Define indices to select
indices = torch.tensor([0, 2])

# Call torch.index_select
selected_tensor = torch.index_select(tensor, 0, indices)

print(selected_tensor)