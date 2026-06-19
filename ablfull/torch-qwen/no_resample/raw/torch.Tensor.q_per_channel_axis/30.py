import torch

# Task 2: Generate input data
tensor = torch.randn(4, 4)
scale_factors = torch.tensor([0.5, 0.75, 1.0, 1.25])
zero_points = torch.tensor([0, 1, 2, 3])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, zero_points=zero_points, axis=0)

print(result)