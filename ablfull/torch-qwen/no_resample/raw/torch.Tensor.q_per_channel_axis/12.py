import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[0.5, 0.7], [0.3, 0.6]], [[0.8, 0.9], [0.1, 0.4]]]])
q_scale = torch.tensor([[[[0.1], [0.2]], [[0.3], [0.4]]]])
q_zero_point = torch.tensor([[[[0], [0]], [[0], [0]]]])

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(tensor, q_scale, q_zero_point)