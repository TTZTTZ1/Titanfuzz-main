import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
scale_factors = [0.5, 0.6, 0.7]
zero_points = [1, 2, 3]

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, zero_points=zero_points, axis=1)