import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_factors = [0.25] * 3

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale_factors=scale_factors)

print(quantized_tensor)