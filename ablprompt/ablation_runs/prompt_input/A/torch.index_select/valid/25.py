import torch

# Create a tensor
tensor = torch.tensor([[1, 2], [3, 4]])

# Define indices to select
indices = torch.tensor([0])

# Call torch.index_select
result = torch.index_select(tensor, 0, indices)

print(result)