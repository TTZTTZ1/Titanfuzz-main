
import torch
input_tensor = torch.randn(5, 5)
result = torch.slogdet(input_tensor)
print(result)
