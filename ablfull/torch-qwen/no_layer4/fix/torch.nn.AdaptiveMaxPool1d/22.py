import torch
output_size = 5
input_tensor = torch.randn(1, 10)
result = torch.nn.AdaptiveMaxPool1d(output_size)(input_tensor)
print(result)