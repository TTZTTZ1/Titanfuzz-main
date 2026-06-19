import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, -2.0], [3.0, -4.0]], dtype=torch.float32)
qscheme = torch.per_tensor_affine

# Task 3: Call the API
result = tensor.q_per_channel_axis(qscheme)
print(result)