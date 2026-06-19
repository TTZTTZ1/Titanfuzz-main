import torch

# Task 2: Generate input data
input_data = torch.randn(10, 3, requires_grad=True)
normalized_shape = [3]

# Task 3: Call the API
layer_norm = torch.nn.LayerNorm(normalized_shape=normalized_shape, eps=1e-05, elementwise_affine=True, bias=True)
output = layer_norm(input_data)