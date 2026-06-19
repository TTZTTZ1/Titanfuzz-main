import torch

# Create tensors satisfying the constraints
a = torch.rand(3, 4, 5)
b = torch.rand(3, 5, 6)
c = torch.rand(3, 4, 6)

# Call the API
result = c.addmm(a.mm(b))