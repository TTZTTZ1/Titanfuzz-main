import torch

# Generate input data
input_tensor = torch.randn(3, 4, dtype=torch.float32)
per_channel_axis = True

# Call the API
quantized_tensor = torch.Tensor.q_per_channel_axis(input_tensor, per_channel_axis)