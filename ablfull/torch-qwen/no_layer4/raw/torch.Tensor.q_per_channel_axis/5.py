import torch

# Task 2: Generate input data
tensor = torch.tensor([[[0.5, -0.2], [0.8, -0.7]], [[0.3, -0.4], [0.6, -0.9]]])
qscheme = torch.per_tensor_affine
dtype = torch.quint8
scale = torch.tensor([0.1, 0.2])
zero_point = torch.tensor([0, 1])

# Task 3: Call the API
result = tensor.q_per_channel_axis(qscheme, dtype=dtype, scale=scale, zero_point=zero_point)
print(result)