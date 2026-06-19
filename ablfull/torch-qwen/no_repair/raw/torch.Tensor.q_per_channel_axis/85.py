import torch

input_data = torch.rand(2, 3, 4, dtype=torch.float)
output = torch.Tensor.q_per_channel_axis(input_data)
print(output)