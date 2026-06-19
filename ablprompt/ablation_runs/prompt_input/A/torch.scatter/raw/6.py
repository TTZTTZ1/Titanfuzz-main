import torch

# Create some input tensors
src = torch.tensor([1, 2, 3])
index = torch.tensor([[0], [2]])
dim = 1

# Call the torch.scatter function
result = torch.zeros(3, 3).scatter_(dim, index, src)

print(result)