import torch

# Prepare valid input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
scale = torch.tensor([0.5, 0.5], dtype=torch.float32)

# Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, scale, axis=0)