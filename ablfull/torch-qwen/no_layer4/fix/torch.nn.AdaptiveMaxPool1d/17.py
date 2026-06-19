import torch
input_tensor = torch.randn(1, 4, 5)
output = torch.nn.AdaptiveMaxPool1d((3,), True)
print(output)