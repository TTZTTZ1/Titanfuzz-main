import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
q_scale = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32)
q_zero_point = torch.tensor([10, 20, 30], dtype=torch.int32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)