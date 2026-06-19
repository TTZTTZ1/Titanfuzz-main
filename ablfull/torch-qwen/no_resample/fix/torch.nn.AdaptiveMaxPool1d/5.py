import torch
input_tensor = torch.randn(1, 64)
output = torch.nn.AdaptiveMaxPool1d(output_size=8)(input_tensor)
print(output)