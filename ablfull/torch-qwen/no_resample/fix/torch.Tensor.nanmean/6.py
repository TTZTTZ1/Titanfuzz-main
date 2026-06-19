import torch
input_tensor = torch.tensor([[1.0, 2.0], [float('nan'), 4.0]])
result = torch.Tensor.nanmean(input_tensor, dim=0, keepdim=True)
print(result)