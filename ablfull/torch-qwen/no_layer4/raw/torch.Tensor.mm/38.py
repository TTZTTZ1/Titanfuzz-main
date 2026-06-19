import torch

# Generate input data
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]], dtype=torch.float)

# Call the API
result = torch.Tensor.mm(a, b)
print(result)