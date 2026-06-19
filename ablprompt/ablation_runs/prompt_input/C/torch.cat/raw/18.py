import torch

# Create a list of tensors
tensors = [torch.randn(2, 3), torch.randn(2, 3), torch.randn(2, 3)]

# Concatenate along the first dimension (rows)
result = torch.cat(tensors, dim=0)

print(result)