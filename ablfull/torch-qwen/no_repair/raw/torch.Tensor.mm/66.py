import torch

# Generate input data
a = torch.tensor([[1., 2.], [3., 4.]])  # 2x2 tensor
b = torch.tensor([[5., 6.], [7., 8.]])  # 2x2 tensor

# Call the API
result = a.mm(b)