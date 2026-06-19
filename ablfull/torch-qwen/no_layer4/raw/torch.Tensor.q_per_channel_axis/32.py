import torch

# Task 2: Generate input data
tensor = torch.randn(4, 5, requires_grad=True)
qscheme = torch.per_tensor_affine
dtype = torch.quint8
scale = 0.5
zero_point = 10

# Task 3: Call the API
result = tensor.q_per_channel_axis(qscheme, dtype=dtype, scale=scale, zero_point=zero_point)