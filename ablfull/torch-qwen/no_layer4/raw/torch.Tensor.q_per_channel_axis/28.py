import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, -2.0], [3.0, -4.0]])
scale = torch.tensor([0.5, 0.5])
zero_point = torch.tensor([0, 0])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale=scale, zero_point=zero_point)