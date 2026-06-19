
import torch
input_tensor = torch.randn(1, 3, 5)
output = torch.nn.AdaptiveMaxPool1d((3,), True)(input_tensor)
print(output)
