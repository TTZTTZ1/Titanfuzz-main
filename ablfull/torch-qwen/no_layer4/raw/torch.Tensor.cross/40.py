import torch

# Generate input data
a = torch.tensor([1, 0, 0])
b = torch.tensor([0, 1, 0])

# Call the API
result = torch.Tensor.cross(a, b)

print(result)