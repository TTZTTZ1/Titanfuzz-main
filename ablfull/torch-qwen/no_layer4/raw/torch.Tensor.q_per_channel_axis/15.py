import torch

# Prepare valid input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
scale = torch.tensor([0.5, 1.0], dtype=torch.float32)
zero_point = torch.tensor([0, 0], dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(scale, zero_point, axis=1)