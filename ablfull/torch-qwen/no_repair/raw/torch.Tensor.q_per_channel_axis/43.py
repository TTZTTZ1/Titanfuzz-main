import torch

# Prepare input data
input_tensor = torch.randint(0, 128, (3, 4), dtype=torch.uint8)
scale_tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
zero_point_tensor = torch.tensor([0, 0, 0], dtype=torch.int32)

# Call the API
result = input_tensor.q_per_channel_axis(scale=scale_tensor, zero_point=zero_point_tensor, axis=0)