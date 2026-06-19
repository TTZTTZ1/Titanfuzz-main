import torch

# Task 2: Generate input data
tensor = torch.randint(0, 100, size=(3, 4), dtype=torch.uint8)
scale_factor = [2, 3, 1]

# Task 3: Call the API
q_tensor = tensor.q_per_channel_axis(scale_factor=scale_factor)