import torch
input_tensor = torch.randn(1, 5, 64)
output = torch.nn.AdaptiveMaxPool1d((32,), return_indices=False)(input_tensor)