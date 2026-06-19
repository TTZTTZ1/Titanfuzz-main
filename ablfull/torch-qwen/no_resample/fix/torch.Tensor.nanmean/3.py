import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])
dim = (0, 1)
keepdim = True
dtype = None
result = torch.Tensor.nanmean(input_tensor, dim=dim, keepdim=keepdim, dtype=dtype)
print(result)