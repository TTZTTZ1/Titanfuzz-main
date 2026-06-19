import torch

# Prepare input data
tensor = torch.randn(3, 4, dtype=torch.float32)
scale_tensor = torch.tensor([0.5, 0.7, 0.9], dtype=torch.float32)

# Call the API
result = tensor.q_per_channel_axis(scale_tensor, axis=1)