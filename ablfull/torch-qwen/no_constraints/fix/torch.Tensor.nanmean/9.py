import torch
input_data = torch.tensor([1.0, 2.0, float('nan'), 4.0])
result = torch.Tensor.nanmean(input_data)
print(result)