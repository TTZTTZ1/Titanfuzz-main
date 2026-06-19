import torch
input_tensor = torch.randn(1, 5, 8)
output = torch.nn.AdaptiveMaxPool1d(output_size=(4,), return_indices=False)(input_tensor)