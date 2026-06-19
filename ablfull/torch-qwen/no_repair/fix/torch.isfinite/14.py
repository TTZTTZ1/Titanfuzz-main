
import torch
input_tensor = torch.randn(3, 3)
result = torch.isfinite(input_tensor)
print(result)
