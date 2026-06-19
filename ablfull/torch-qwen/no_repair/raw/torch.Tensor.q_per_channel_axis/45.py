import torch

# Generate input data
tensor = torch.rand(3, 4)
axis = 0

# Call the API
result = tensor.q_per_channel_axis(axis=axis)
print(result)