import torch

# Create some tensors
tensor = torch.tensor([1, 2, 3, 4])
index = torch.tensor([[0], [2]])
src = torch.tensor([99, 88])

# Call torch.scatter
result = tensor.scatter_(1, index, src)

print(result)