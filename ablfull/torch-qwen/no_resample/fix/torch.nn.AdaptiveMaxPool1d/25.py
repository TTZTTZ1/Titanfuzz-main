import torch
output_size = 3
input_tensor = torch.randn(1, 5)
result = torch.nn.AdaptiveMaxPool1d(output_size)(input_tensor)
print(result)