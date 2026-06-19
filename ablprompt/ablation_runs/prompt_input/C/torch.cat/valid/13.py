import torch

# Create some example tensors
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
tensor3 = torch.tensor([[9, 10], [11, 12]])

# Concatenate tensors along the first dimension (rows)
result = torch.cat((tensor1, tensor2, tensor3), dim=0)

print(result)