import torch

# Generate input data
tensor = torch.randn(4, 3, 224, 224)
axis = 0

# Call the API
result = tensor.q_per_channel_axis(axis=axis)