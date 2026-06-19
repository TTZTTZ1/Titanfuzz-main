import torch
data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])
result = torch.nanmean(data)
print(result)