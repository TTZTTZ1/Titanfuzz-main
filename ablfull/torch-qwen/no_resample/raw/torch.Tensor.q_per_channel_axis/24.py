import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_factors = [0.5] * 3
zero_points = [128] * 3

# Task 3: Call the API
quantized_tensor = input_tensor.q_per_channel_axis(scale_factors=scale_factors, zero_points=zero_points, axis=1)