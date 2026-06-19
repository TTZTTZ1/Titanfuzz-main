import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 5, 8)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=(4,), return_indices=False)(input_tensor)