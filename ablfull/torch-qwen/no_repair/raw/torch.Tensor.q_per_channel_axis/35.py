import torch

# Generate input data
tensor = torch.tensor([[0.5, -0.5], [0.75, -0.25]])
scale_factors = torch.tensor([0.25, 0.5])

# Call the API
result = tensor.q_per_channel_axis(scale_factors)