import torch

# Generate input data
tensor = torch.randn(4, 3, 224, 224)
qscheme = torch.per_tensor_affine

# Call the API
result = tensor.q_per_channel_axis(qscheme)