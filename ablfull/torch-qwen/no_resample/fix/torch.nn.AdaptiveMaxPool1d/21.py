import torch
input_tensor = torch.randn(1, 5, 64)
output = torch.nn.AdaptiveMaxPool1d((8,), True)(input_tensor)
print(output)