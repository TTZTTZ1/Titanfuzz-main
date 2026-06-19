import torch

# Prepare valid input data
a = torch.tensor([[1., 2.], [3., 4.]])
b = torch.tensor([[5., 6.]])

# Call the API
result = torch.Tensor.mm(a, b)
print(result)