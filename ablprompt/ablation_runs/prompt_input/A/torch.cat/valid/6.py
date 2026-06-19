import torch

# Create two tensors
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])

# Concatenate them along dimension 0 (rows)
result = torch.cat((tensor1, tensor2), dim=0)

print(result)