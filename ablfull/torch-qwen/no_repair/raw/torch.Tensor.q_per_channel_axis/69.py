import torch

# Prepare valid input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
scale_factor = [1.0, 1.5, 2.0]
zero_point = [0, 0, 0]

# Call the API
output_tensor = torch.Tensor.q_per_channel_axis(input_tensor, scale_factor, zero_point)