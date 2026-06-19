import torch

# Create a tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Define indices to select from the first dimension
indices = torch.tensor([0, 1])

# Call torch.index_select
result = torch.index_select(tensor, 0, indices)

print(result)