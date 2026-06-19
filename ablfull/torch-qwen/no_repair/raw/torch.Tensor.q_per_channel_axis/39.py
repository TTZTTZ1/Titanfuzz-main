import torch

input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
q_per_channel_axis = 0

result = torch.Tensor.q_per_channel_axis(input_tensor, q_per_channel_axis)
print(result)