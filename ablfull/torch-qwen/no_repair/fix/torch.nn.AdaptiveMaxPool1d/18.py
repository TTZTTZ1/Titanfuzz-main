
import torch
input_tensor = torch.randn(1, 10)
output = torch.nn.AdaptiveMaxPool1d((5,), return_indices=False)(input_tensor)
