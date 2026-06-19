import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4, 5)
axis = 1

# Call the API
quantized_tensor = input_tensor.q_per_channel_axis(axis=axis)