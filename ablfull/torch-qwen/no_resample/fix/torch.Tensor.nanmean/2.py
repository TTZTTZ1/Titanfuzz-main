import torch
data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])
result = torch.Tensor.nanmean(data, dim=1, keepdim=True)
print(result)