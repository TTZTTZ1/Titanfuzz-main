import torch

# Generate input data
tensor = torch.randn(3, 4, requires_grad=True)
scale = torch.tensor([0.5, 1.0, 1.5], dtype=torch.float32)

# Call the API
result = tensor.q_per_channel_axis(scale)