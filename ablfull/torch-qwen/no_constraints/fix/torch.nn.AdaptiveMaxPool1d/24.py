import torch
input_tensor = torch.randn(1, 4, 5)
output = torch.nn.AdaptiveMaxPool1d((2,), return_indices=True)(input_tensor)