import torch
input_tensor = torch.randn(1, 10)
output = torch.nn.AdaptiveMaxPool1d(output_size=5)(input_tensor)