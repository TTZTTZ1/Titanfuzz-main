import torch

# Prepare valid input data
tensor = torch.randn(4, 3, 224, 224)
dtype = torch.quint8
scale = torch.tensor([0.5] * 3)
zero_point = torch.tensor([128] * 3)

# Call the API
result = tensor.q_per_channel_axis(dtype=dtype, scale=scale, zero_point=zero_point, axis=0)