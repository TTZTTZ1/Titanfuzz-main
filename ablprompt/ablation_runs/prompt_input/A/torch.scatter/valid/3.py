import torch

# Create some tensors
tensor = torch.randn(3, 3)
index = torch.tensor([[0, 2], [1, 0]])
source = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Call torch.scatter
result = tensor.scatter_(1, index, source)

print(result)