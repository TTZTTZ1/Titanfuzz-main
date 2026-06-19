import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
scale_tensor = torch.tensor([0.5, 0.6, 0.7])
zero_point_tensor = torch.tensor([1, 2, 3])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale=scale_tensor, zero_point=zero_point_tensor, axis=1)