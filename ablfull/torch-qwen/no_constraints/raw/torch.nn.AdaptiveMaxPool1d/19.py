import torch

# Task 2: Generate input data
input_data = torch.randn(1, 64, 50)

# Task 3: Call the API
output = torch.nn.AdaptiveMaxPool1d(output_size=10)(input_data)