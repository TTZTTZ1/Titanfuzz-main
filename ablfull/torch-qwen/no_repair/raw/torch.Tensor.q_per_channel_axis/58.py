import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4, dtype=torch.float32)
axis = 0

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, axis=axis)