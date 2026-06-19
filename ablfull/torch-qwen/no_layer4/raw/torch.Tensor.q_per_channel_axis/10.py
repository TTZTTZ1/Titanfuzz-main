import torch

# Generate input data
tensor = torch.randn(4, 3, 8, 8)
q_scale = torch.tensor([0.5, 1.0, 1.5])
q_zero_point = torch.tensor([-1, 0, 1])

# Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point, axis=1)