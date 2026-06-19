import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[0.1, 0.2], [0.3, 0.4]], [[0.5, 0.6], [0.7, 0.8]]]])
scale_factors = torch.tensor([[0.1, 0.2]])

# Task 3: Call the API
result = tensor.q_per_channel_axis(scale_factors=scale_factors)
print(result)