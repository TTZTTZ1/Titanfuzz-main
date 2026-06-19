import torch
input_tensor = torch.tensor([[10, 5], [3, 8]], dtype=torch.int)
result = torch.Tensor.cummin(input_tensor, dim=0)
print(result)