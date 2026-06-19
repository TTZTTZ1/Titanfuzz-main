import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[[0.5, -0.5], [0.3, -0.3]], [[0.8, -0.8], [0.6, -0.6]]])
scale = torch.tensor([0.1, 0.2])

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, scale)