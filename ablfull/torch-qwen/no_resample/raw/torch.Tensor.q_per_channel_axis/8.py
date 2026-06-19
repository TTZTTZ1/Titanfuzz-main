import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 256, 256)
scale_factor = [0.1, 0.2, 0.3]
zero_point = [0, 0, 0]

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factor=scale_factor, zero_point=zero_point, axis=1)