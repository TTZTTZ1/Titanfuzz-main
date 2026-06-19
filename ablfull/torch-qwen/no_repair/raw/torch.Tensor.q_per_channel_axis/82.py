import torch

# Task 2: Generate input data
tensor = torch.randn(4, 3, 224, 224)
scale_factors = torch.tensor([0.5] * 3)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale_factors=scale_factors)