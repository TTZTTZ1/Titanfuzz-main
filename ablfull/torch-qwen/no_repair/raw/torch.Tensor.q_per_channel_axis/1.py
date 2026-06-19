import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
q_per_channel_axis = True

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(q_per_channel_axis)