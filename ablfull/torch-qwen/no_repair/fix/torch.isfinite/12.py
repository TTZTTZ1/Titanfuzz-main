
import torch
input_tensor = torch.randn(5, 5)
result = torch.isfinite(input_tensor)
print(result)
