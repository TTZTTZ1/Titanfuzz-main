import torch

# Prepare valid input data
tensor = torch.tensor([[[0.5, -0.5], [0.2, -0.2]], [[0.8, -0.8], [0.6, -0.6]]])
axis = 0

# Call the API
result = tensor.q_per_channel_axis(axis)