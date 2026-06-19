import torch

# Task 2: Generate input data
tensor = torch.tensor([[0.5, 0.7], [0.3, 0.8]], dtype=torch.float32)

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis()