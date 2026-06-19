import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (3, 4), dtype=torch.uint8)
scale_factors = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors)