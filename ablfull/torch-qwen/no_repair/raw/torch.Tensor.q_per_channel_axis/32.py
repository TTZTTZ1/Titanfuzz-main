import torch

# Generate input data
tensor = torch.randn(4, 3, 256, 256)
q_scale = torch.tensor([0.1, 0.2, 0.3])
q_zero_point = torch.tensor([0, 0, 0])

# Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)