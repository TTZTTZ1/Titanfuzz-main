import torch
data = torch.tensor([[1.0, 2.0, float('nan')], [4.0, float('nan'), 6.0]])
dim = (0, 1)
keepdim = True
dtype = None
result = torch.Tensor.nanmean(data, dim=dim, keepdim=keepdim, dtype=dtype)
print(result)