import torch

# Task 2: Generate input data
tensor = torch.tensor([[0.5, -0.5], [1.0, -1.0]], dtype=torch.float32)
scale_tensor = torch.tensor([0.5, 1.0], dtype=torch.float32)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale_tensor, axis=0)