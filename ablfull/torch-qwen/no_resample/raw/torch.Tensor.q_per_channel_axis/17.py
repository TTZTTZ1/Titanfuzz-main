import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[[0.5, -0.5], [0.75, -0.25]], [[0.25, -0.75], [0.5, -0.5]]])
q_scale = torch.tensor([0.1, 0.2])
q_zero_point = torch.tensor([0, 128])

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, q_scale, q_zero_point)