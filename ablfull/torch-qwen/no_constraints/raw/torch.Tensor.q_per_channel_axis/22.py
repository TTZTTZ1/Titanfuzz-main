import torch

# Prepare valid input data
tensor = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])
dtype = torch.qint8
scale = torch.tensor([0.1, 0.2], dtype=torch.float32)
zero_point = torch.tensor([10, 20], dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(dtype=dtype, scale=scale, zero_point=zero_point, axis=0)