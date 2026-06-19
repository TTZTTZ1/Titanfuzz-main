
import torch
input_data = torch.randn(3, 4)
layer_norm = torch.nn.LayerNorm(normalized_shape=(3, 4))
output = layer_norm(input_data)
