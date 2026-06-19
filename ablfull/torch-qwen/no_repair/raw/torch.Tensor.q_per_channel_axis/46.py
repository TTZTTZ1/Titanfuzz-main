import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
scale_factors = torch.tensor([0.5, 0.25])
zero_points = torch.tensor([1, -1], dtype=torch.int8)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(scale_factors=scale_factors, zero_points=zero_points, axis=0)
print(quantized_tensor)