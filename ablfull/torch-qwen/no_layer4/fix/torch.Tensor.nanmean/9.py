import torch
input_tensor = torch.tensor([[1.0, float('nan')], [2.0, 3.0]])
dim = 0
keepdim = True
result = torch.Tensor.nanmean(input_tensor, dim=dim, keepdim=keepdim)
print(result)