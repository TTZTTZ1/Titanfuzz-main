import torch

# Generate input data
input_tensor = torch.randn(4, 3, 224, 224)
qscheme = torch.per_channel_affine_dynamic

# Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, qscheme)