import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 5, requires_grad=True)
qscheme = torch.per_channel_affine_dynamic
dtype = torch.qint8
qscheme_kwargs = {'qscheme': qscheme, 'dtype': dtype}

# Task 3: Call the API
result = input_tensor.q_per_channel_axis(**qscheme_kwargs)