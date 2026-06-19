import torch

# Generate input data
tensor = torch.rand(4, 3, 8, 8)
qscheme = torch.per_tensor_affine

# Call the API
result = tensor.q_per_channel_axis(qscheme)