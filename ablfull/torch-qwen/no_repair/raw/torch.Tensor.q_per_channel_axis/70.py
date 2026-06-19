import torch

# Task 2: Generate input data
tensor = torch.randn(3, 4, dtype=torch.float32)
dtype = torch.qint8
qscheme = torch.per_channel_affine_qint8
scale = [0.5, 0.6, 0.7]
zero_point = [10, 11, 12]

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale=scale, zero_point=zero_point, dtype=dtype, qscheme=qscheme)

print(result)