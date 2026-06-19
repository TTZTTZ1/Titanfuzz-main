import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[[0.5, -0.3], [0.8, -0.7]], [[-0.2, 0.4], [-0.6, 0.9]]], dtype=torch.float32)
scale_factor = 0.1
zero_point = torch.tensor([[0, 0], [0, 0]])

# Task 3: Call the API
output_tensor = torch.Tensor.q_per_channel_axis(input_tensor, scale_factor=scale_factor, zero_point=zero_point, axis=0)

print(output_tensor)