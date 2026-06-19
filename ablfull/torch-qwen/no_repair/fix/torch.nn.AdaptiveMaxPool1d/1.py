
import torch
input_tensor = torch.randn(1, 4, 5)
output = torch.nn.AdaptiveMaxPool1d((2,), True)(input_tensor)
print(output)
