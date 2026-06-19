import torch

# Prepare valid input data
tensor = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])
qscheme = torch.per_tensor_affine
dtype = torch.qint8
scale = 2.0
zero_point = 1

# Call the API
result = tensor.q_per_channel_axis(qscheme, dtype, scale, zero_point)
print(result)