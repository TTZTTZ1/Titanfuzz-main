import torch
normalized_shape = [3]
input_tensor = torch.randn(4, 3)
layer_norm = torch.nn.LayerNorm(normalized_shape)
output_tensor = layer_norm(input_tensor)