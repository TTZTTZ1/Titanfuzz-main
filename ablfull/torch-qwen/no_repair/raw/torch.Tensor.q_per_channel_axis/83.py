import torch

# Prepare input data
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
q_scale = torch.tensor([0.5, 0.25])
zero_point = torch.tensor([0, 0])

# Call the API
quantized_tensor = input_tensor.q_per_channel_axis(q_scale, zero_point)

print(quantized_tensor)