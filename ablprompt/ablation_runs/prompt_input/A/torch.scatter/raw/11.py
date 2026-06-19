import torch

# Create some tensors
tensor = torch.ones(3, 4)
index = torch.tensor([[0, 2], [2, 0]])
source = torch.tensor([[1, 1], [1, 1]])

# Call torch.scatter
result = tensor.scatter_(1, index, source)

print(result)