import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4, 5)

# Task 3: Call the API
quantized_tensor, scale_factors, zero_points = torch.Tensor.q_per_channel_axis(input_tensor)