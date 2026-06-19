import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
scale_tensor = torch.tensor([0.5, 0.6, 0.7], dtype=torch.float32)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale_tensor=scale_tensor, axis=1)