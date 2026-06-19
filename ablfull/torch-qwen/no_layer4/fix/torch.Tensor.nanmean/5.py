import torch
tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])
result = torch.Tensor.nanmean(tensor, dim=1, keepdim=True)
print(result)