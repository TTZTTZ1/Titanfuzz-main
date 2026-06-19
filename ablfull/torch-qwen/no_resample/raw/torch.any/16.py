import torch

input_tensor = torch.tensor([[-1.0, -2.0], [3.0, 4.0]])
dim = 1
keepdim = True

result = torch.any(input_tensor, dim=dim, keepdim=keepdim)
print(result)