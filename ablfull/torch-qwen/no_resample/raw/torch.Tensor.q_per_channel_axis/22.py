import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[0.5, -0.5], [0.75, -0.25]], [[0.25, -0.75], [0.125, -0.625]]]])
scale_tensor = torch.tensor([[1.0, 1.0]])
zero_point_tensor = torch.tensor([[0, 0]])

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(tensor, scale_tensor, zero_point_tensor)