import torch
input_tensor = torch.randn(1, 4, 8)
output = torch.nn.AdaptiveMaxPool1d(output_size=4)(input_tensor)
print(output)