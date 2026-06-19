import torch

# Prepare valid input data
tensor = torch.randn(4, 3, 8, 8)
q_scale = torch.tensor([0.5, 0.75, 1.0])
q_zero_point = torch.tensor([0, 0, 0])

# Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)