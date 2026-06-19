import torch

# Prepare valid input data
tensor = torch.tensor([[1.0, -1.0], [2.0, -2.0]], dtype=torch.float32)
qscheme = torch.per_tensor_affine
dtype = torch.quint8

# Call the API
result = tensor.q_per_channel_axis(qscheme, dtype=dtype)

print(result)