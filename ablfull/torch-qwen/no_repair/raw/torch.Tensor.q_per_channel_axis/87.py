import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 16, 16)
scales = torch.tensor([0.5, 0.6, 0.7])
zero_points = torch.tensor([0, 1, 2])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scales=scales, zero_points=zero_points, axis=0)

print(result)