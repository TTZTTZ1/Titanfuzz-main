import torch
input_tensor = torch.tensor([[1, 2], [0, 4]], dtype=torch.float32)
result = input_tensor.cummin(1)
print(result)