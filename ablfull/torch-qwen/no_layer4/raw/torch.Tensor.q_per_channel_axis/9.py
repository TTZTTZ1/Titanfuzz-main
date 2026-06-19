import torch

# Prepare valid input data
tensor = torch.randn(4, 3, 256, 256)
dtype = torch.quint8
scale = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32)
zero_point = torch.tensor([128, 127, 126], dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(dtype=dtype, scale=scale, zero_point=zero_point, axis=1)