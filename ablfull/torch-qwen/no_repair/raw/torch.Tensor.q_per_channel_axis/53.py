import torch

# Prepare valid input data
tensor = torch.tensor([[1.0, -1.0], [2.0, -2.0]])
axis = 0

# Call the API
result = tensor.q_per_channel_axis(axis)