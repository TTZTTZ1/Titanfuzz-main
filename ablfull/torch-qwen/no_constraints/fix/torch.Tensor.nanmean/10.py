import torch
input_data = torch.tensor([[1.0, 2.0], [3.0, float('nan')]])
result = torch.nanmean(input_data)
print(result)