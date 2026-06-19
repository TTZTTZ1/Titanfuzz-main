import torch

# Prepare valid input data
tensor = torch.randint(0, 256, (4, 4), dtype=torch.uint8)
axis = 0

# Call the API
result = tensor.q_per_channel_axis(axis)