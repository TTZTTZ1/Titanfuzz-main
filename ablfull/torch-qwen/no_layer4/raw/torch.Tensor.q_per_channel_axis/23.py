import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_tensor = torch.tensor([0.5, 0.5, 0.5], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_tensor)