import torch

# Create some example tensors
data = torch.tensor([[1, 2], [3, 4]])
index = torch.tensor([[0, 1], [1, 0]])
src = torch.tensor([[5, 6], [7, 8]])

# Call torch.scatter
result = torch.scatter(data, 1, index, src)

print(result)