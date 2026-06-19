import torch
input_tensor = torch.tensor([[1.0, float('nan')], [float('nan'), 4.0]])
dim = (0, 1)
keepdim = True
dtype = None
result = torch.Tensor.nanmean(input_tensor, dim=dim, keepdim=keepdim, dtype=dtype)
print(result)