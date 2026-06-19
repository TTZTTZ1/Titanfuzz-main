import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[0.5, 1.0], [1.5, 2.0]], [[2.5, 3.0], [3.5, 4.0]]]], dtype=torch.float32)

# Task 3: Call the API
result = tensor.q_per_channel_axis(qscheme=torch.per_tensor_affine)