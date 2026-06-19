import torch

input_tensor = torch.randn(1, 3, 5)
output_size = (2,)
api_call = torch.nn.AdaptiveMaxPool1d(output_size)
result = api_call(input_tensor)