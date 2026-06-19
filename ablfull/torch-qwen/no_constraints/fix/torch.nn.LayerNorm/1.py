import torch
input_tensor = torch.randn(3, 4)
normalized_shape = [4]
layer_norm = torch.nn.LayerNorm(normalized_shape=normalized_shape)
output_tensor = layer_norm(input_tensor)