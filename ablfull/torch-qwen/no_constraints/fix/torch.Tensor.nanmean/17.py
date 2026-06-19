import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, float('nan')]], dtype=torch.float32)
result = torch.Tensor.nanmean(input_tensor)
print(result)