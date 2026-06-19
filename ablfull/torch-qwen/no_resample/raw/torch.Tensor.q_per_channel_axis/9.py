import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[0.5, 0.7], [0.8, 0.9]], [[0.1, 0.2], [0.3, 0.4]]]])
scale_tensor = torch.tensor([[[[0.1, 0.1], [0.1, 0.1]], [[0.1, 0.1], [0.1, 0.1]]]])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_tensor)