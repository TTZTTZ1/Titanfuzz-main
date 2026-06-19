import torch

# Task 2: Generate input data
input_tensor = torch.rand(4, 8, 64, 64)  # Example shape for q_per_channel_axis
dtype = torch.quint8  # Example dtype for q_per_channel_axis

# Task 3: Call the API
result = torch.Tensor.q_per_channel_axis(input_tensor, dtype=dtype)