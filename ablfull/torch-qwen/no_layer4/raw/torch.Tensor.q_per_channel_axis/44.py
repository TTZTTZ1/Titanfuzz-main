import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
dtype = torch.qint8
qscheme = torch.per_tensor_affine
scale = 0.5
zero_point = 3

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale, zero_point, dtype=dtype, qscheme=qscheme)