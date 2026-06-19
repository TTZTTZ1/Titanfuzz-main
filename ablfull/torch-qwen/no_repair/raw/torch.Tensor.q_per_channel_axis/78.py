import torch

# Task 2: Generate input data
tensor = torch.rand(4, 3, 5)
scale_factors = torch.tensor([0.5, 1.0, 1.5])
zero_points = torch.tensor([0, 128, 64])

# Task 3: Call the API
result = torch.ops.aten.q_per_channel_axis.default(tensor, scale_factors, zero_points, axis=1)
print(result)