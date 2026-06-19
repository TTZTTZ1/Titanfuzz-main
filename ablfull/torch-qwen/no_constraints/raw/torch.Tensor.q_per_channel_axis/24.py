import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_tensor = torch.tensor([1.0, 1.0, 1.0], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale=scale_tensor, axis=1)