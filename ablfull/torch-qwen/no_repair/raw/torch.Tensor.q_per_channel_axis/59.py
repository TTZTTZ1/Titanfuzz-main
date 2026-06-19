import torch

# Prepare valid input data
tensor = torch.randint(0, 256, (4, 3, 32, 32), dtype=torch.uint8)
scale_factors = torch.tensor([0.1, 0.1, 0.1])

# Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors)