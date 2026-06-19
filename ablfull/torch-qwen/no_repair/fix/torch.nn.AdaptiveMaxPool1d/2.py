
import torch
input_tensor = torch.randn(1, 5, 64)
output = torch.nn.AdaptiveMaxPool1d(output_size=32)(input_tensor)
