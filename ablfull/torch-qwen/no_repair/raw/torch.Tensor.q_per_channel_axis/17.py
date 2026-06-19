import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
scale_factors = torch.tensor([0.5, 0.75], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, axis=0)