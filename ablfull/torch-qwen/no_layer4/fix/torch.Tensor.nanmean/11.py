import torch
input_tensor = torch.tensor([[1.0, 2.0], [float('nan'), 4.0]])
dim = 1
keepdim = True
result = torch.Tensor.nanmean(input_tensor, dim=dim, keepdim=keepdim)
print(result)