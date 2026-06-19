import torch

# Generate input data
tensor = torch.tensor([[[0.5, -0.5], [0.2, -0.2]], [[0.8, -0.8], [0.4, -0.4]]])
q_scale = torch.tensor([0.25, 0.125])

# Call the API
result = tensor.q_per_channel_axis(q_scale, axis=2)

print(result)