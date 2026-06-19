import torch
input_tensor = torch.randn(1, 4, 6)
output = torch.nn.AdaptiveMaxPool1d(output_size=2)(input_tensor)
print(output)