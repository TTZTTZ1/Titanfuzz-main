import torch

# Task 2: Generate input data
tensor = torch.tensor([[[0.5, -0.2], [0.8, -0.4]], [[0.3, -0.6], [0.7, -0.9]]], dtype=torch.float32)
scale = torch.tensor([0.1, 0.2], dtype=torch.float32)
zero_point = torch.tensor([0, 128], dtype=torch.int32)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale=scale, zero_point=zero_point, axis=1)