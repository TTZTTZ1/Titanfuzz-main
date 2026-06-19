import torch
input_tensor = torch.rand(5, 5)
result = torch.isfinite(input_tensor)
print(result)