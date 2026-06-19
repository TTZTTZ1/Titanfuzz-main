import torch

# Prepare valid input data
input_tensor = torch.randn(3, 4, dtype=torch.float32)
scale = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32)

# Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, scale)