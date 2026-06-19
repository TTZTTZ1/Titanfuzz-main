import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_factors = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, axis=(0, 1))