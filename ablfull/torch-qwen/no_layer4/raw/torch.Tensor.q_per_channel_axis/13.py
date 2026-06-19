import torch

# Prepare valid input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
axis = 1

# Call the API
result = tensor.q_per_channel_axis(axis)