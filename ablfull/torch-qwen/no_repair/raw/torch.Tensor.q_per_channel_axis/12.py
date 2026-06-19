import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1.0, -2.0], [3.0, -4.0]], dtype=torch.float32)
scale_factors = torch.tensor([0.5, 1.0], dtype=torch.float32)

# Task 3: Call the API
quantized_tensor = torch.Tensor.q_per_channel_axis(input_tensor, scale_factors, axis=0)