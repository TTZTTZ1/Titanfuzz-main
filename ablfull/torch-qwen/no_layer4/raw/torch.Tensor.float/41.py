import torch

# Task 2: Generate input data
input_data = torch.randn(4, 4)

# Task 3: Call the API
output_data = input_data.float(memory_format=torch.channels_last)