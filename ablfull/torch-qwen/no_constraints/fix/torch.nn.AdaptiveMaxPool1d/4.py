import torch
input_tensor = torch.randn(1, 64, 8)
output = torch.nn.AdaptiveMaxPool1d((4,), return_indices=False)(input_tensor)