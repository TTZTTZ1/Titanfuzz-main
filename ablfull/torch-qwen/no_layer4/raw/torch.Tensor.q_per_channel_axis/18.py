import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_factors = torch.tensor([1.0, 1.0, 1.0], dtype=torch.float32)

# Task 3: Call the API
quantized_tensor = torch.Tensor.q_per_channel_axis(input_tensor, scale_factors)