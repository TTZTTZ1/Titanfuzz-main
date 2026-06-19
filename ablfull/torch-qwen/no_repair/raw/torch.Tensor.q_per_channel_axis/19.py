import torch

# Task 2: Generate input data
tensor = torch.tensor([[1.0, -2.0], [3.0, -4.0]], dtype=torch.float32)
qscheme = torch.per_tensor_affine

# Task 3: Call the API
quantized_tensor = tensor.quantize_per_channel(qscheme, scales=[0.5, 1.0], zero_points=[0, 0], axis=1)

print(quantized_tensor)