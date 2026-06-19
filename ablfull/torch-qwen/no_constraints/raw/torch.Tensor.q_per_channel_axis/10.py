import torch

# Task 2: Generate input data
tensor = torch.tensor([[[0.5, -0.5], [0.3, -0.3]], [[0.4, -0.4], [0.2, -0.2]]])
scale_factors = torch.tensor([[0.1, 0.1], [0.2, 0.2]])
zero_points = torch.tensor([[0, 0], [1, 1]])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, zero_points=zero_points)