import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
scale_tensor = torch.tensor([0.5, 0.5], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_tensor, axis=0)