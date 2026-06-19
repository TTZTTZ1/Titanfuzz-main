import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1.0, -2.0], [3.0, -4.0]], dtype=torch.float32)
qscheme = torch.per_channel_affine_float_qint8

# Task 3: Call the API
output_tensor = input_tensor.q_per_channel_axis(qscheme)

print(output_tensor)