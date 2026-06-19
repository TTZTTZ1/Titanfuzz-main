import torch
input_data = torch.randn(1, 4, 5)
output = torch.nn.AdaptiveMaxPool1d(output_size=3)(input_data)
print(output)