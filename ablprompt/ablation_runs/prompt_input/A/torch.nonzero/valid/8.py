import torch

# Create a tensor
tensor = torch.tensor([[0, 1, 2], [3, 0, 5]])

# Call torch.nonzero on the tensor
nonzero_indices = torch.nonzero(tensor)

print(nonzero_indices)