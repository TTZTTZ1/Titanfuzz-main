import torch
input_data = torch.randn(1, 64, 50)
output = torch.nn.AdaptiveMaxPool1d(output_size=10)(input_data)