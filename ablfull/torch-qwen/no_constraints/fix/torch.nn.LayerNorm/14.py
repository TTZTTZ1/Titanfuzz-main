import torch
normalized_shape = [3]
input_data = torch.randn(4, 3)
layer_norm = torch.nn.LayerNorm(normalized_shape)
output = layer_norm(input_data)