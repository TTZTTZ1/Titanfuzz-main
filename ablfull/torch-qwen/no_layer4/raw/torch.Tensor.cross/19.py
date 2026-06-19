import torch

# Generate input data
a = torch.tensor([[1, 0, 0], [0, 1, 0]], dtype=torch.float32)
b = torch.tensor([[0, 0, 1], [1, 0, 0]], dtype=torch.float32)

# Call the API
result = a.cross(b, dim=2)
print(result)