import torch

# Task 2: Generate input data
input_data = torch.randn(3, 4)

# Task 3: Call the API
result = input_data.float(memory_format=torch.channels_last)