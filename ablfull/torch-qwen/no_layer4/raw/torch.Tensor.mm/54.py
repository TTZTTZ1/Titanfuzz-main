import torch

# Prepare valid input data
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)

# Call the target API
result = torch.Tensor.mm(a, b)