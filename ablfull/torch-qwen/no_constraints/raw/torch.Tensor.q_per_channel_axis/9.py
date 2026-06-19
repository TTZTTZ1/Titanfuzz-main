import torch

# Prepare valid input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
q_scheme = torch.per_tensor_affine
dtype = torch.quint8
scale = torch.tensor([0.5, 1.0])
zero_point = torch.tensor([0, 128])

# Call the API
result = tensor.q_per_channel_axis(qscheme=q_scheme, dtype=dtype, scale=scale, zero_point=zero_point)