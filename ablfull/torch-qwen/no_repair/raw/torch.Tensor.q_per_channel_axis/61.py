import torch

# Task 2: Generate input data
tensor = torch.tensor([[[1.0, -2.0], [3.0, -4.0]], [[5.0, -6.0], [7.0, -8.0]]])
q_params = {"dtype": torch.quint8}

# Task 3: Call the API
quantized_tensor = tensor.q_per_channel_axis(**q_params)