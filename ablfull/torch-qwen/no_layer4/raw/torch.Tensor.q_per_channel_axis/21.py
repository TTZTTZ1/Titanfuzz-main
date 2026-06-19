import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
scale_factor = [0.1, 0.2, 0.3]
zero_point = [10, 20, 30]

# Task 3: Call the API
quantized_tensor = torch.Tensor.q_per_channel_axis(input_tensor, scale_factor, zero_point)