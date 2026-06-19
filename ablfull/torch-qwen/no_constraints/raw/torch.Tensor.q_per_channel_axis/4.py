import torch

# Task 2: Generate input data
tensor = torch.tensor([[0.5, -0.2], [0.8, 0.1]], dtype=torch.float32)
scale_factors = torch.tensor([0.1, 0.2], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors, axis=0)

print(result)