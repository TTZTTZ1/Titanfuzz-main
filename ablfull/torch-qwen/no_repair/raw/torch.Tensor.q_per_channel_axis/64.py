import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 8), dtype=torch.uint8)
scale_factors = [1.0, 0.5, 2.0]
zero_points = [0, 128, 64]

# Task 3: Call the API
result = torch.ops.torchvision.quantization_ops.q_per_channel_axis(tensor, scale_factors, zero_points, axis=1)
print(result)