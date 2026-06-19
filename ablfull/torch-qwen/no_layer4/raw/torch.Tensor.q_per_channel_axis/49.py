import torch

# Generate input data
tensor = torch.rand(4, 8, dtype=torch.float32)
scale_tensor = torch.tensor([0.5] * 4, dtype=torch.float32)
zero_point_tensor = torch.tensor([10] * 4, dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(scale=scale_tensor, zero_point=zero_point_tensor)