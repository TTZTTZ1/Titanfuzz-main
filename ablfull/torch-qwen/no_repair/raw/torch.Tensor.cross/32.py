import torch

# Prepare input data
a = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = torch.tensor([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

# Call the API
result = a.cross(b, dim=0)

print(result)