import torch

# Generate input data
tensor = torch.rand(3, 4, 5)
scale = torch.tensor([0.1, 0.2, 0.3])
zero_point = torch.tensor([0, 1, 2])

# Call the API
result = tensor.q_per_channel_axis(scale=scale, zero_point=zero_point)