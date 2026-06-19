
import torch
input_tensor = torch.randn(1, 16)
output = torch.nn.AdaptiveMaxPool1d((8,), return_indices=False)(input_tensor)
