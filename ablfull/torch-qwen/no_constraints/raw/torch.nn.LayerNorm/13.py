import torch

# Task 2: Generate input data
input_data = torch.randn(3, 4)
normalized_shape = [4]

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape=normalized_shape, eps=1e-05, elementwise_affine=True, bias=True)
output = layer_norm(input_data)