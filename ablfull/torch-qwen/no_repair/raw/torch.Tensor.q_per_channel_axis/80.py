import torch

# Task 2: Generate input data
tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
dtype = torch.quint8
per_channel_scales = torch.tensor([0.5, 0.75], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(tensor, dtype=dtype, per_channel_scales=per_channel_scales, axis=0)