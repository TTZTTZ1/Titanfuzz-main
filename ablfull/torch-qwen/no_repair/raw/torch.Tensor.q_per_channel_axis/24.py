import torch

# Prepare valid input data
tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
q_scale = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float32)
q_zero_point = torch.tensor([0, 0, 0], dtype=torch.int32)

# Call the API
result = tensor.q_per_channel_axis(q_scale, q_zero_point)