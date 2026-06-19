import torch

# Generate input data
tensor = torch.randn(3, 4)
qmin = -10
qmax = 10

# Call the API
result = tensor.q_per_channel_axis(qmin=qmin, qmax=qmax)