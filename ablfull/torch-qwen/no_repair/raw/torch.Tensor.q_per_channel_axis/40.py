import torch

# Generate input data
tensor = torch.randn(3, 4)
qscheme = torch.per_tensor_affine

# Call the API
result = tensor.q_per_channel_axis(qscheme)