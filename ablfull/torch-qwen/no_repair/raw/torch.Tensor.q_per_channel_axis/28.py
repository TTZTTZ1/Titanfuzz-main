import torch

# Task 2: Generate input data
tensor = torch.randn(3, 4, 5)
scale_factor = 0.5
zero_point = 0

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factor=scale_factor, zero_point=zero_point, axis=1)