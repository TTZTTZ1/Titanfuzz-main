import torch
input_tensor = torch.randn(1, 5, 6)
output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_tensor)
print(output)