import torch
input_tensor = torch.randn(1, 3, 5)
output = torch.nn.AdaptiveMaxPool1d((1,), return_indices=True)(input_tensor)