import torch

# Generate input data
input_tensor = torch.randn(4, 3, 8, 8)
qmin = 0
qmax = 255

# Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, qmin, qmax)