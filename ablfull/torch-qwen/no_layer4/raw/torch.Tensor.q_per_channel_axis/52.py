import torch

# Task 2: Generate input data
tensor = torch.tensor([[[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]]])
scale_factor = 2
zero_point = 0
dtype = torch.quint8

# Task 3: Call the API
quantized_tensor = tensor.quantize_per_channel(scale_factor, zero_point, axis=1, dtype=dtype)