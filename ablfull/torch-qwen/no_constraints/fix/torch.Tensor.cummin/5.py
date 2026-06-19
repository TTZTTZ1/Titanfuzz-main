import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
result = torch.Tensor.cummin(input_tensor, dim=0)
print(result)