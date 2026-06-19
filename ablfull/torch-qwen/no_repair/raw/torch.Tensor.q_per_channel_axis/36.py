import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)

# Task 3: Call the API
result = input_tensor.q_per_channel_axis()