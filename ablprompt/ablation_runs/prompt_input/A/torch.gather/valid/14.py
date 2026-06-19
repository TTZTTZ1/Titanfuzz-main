import torch

# Create a tensor and an index tensor
tensor = torch.tensor([[1, 2], [3, 4]])
index = torch.tensor([[0, 1], [1, 0]])

# Use torch.gather to gather values from the tensor using the index
result = torch.gather(tensor, 1, index)

print(result)