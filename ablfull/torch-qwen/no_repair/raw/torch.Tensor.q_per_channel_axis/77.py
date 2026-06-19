import torch

# Generate valid input data
tensor = torch.randint(0, 256, (2, 3), dtype=torch.uint8)
scale_factors = torch.tensor([0.1, 0.2], dtype=torch.float32)

# Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, axis=0)