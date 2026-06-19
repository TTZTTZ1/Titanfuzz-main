import torch

# Task 2: Generate input data
tensor = torch.tensor([[-1.0, 0.0], [0.5, 1.0]])
dtype = torch.qint8
scheme = torch.per_tensor_affine
q_per_channel_axis = True
axis = -1

# Task 3: Call the API
result = tensor.quantize_per_channel(tensor, dtype=dtype, q_per_channel_axis=q_per_channel_axis, axis=axis)
print(result)