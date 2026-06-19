import torch

# Generate input data
input_tensor = torch.randn(4, 3, 224, 224)
q_per_channel_axis = True

# Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, q_per_channel_axis)