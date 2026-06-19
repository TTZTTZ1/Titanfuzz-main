import torch

# Generate input data
a = torch.randn(3, 4)
b = torch.randn(4, 2)

# Call the API
result = torch.Tensor.mm(a, b)
print(result)