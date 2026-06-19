import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, size=(4, 3, 224, 224), dtype=torch.uint8)
scale_factor = [1.0, 1.0, 1.0]
zero_point = [0, 0, 0]

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factor=scale_factor, zero_point=zero_point, axis=0)