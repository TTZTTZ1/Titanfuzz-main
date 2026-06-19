import torch
input_tensor = torch.randn(1, 3, 5)
output = torch.nn.AdaptiveMaxPool1d((2,), return_indices=False)(input_tensor)