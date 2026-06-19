import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
dtype = torch.quint8
qscheme = torch.per_channel_affine_float_qscheme

# Task 3: Call the API
result = tensor.q_per_channel_axis(dtype=dtype, qscheme=qscheme)

print(result)