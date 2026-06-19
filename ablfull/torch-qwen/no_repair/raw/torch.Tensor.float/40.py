import torch

# Task 2: Generate input data
input_data = torch.tensor([1, 2, 3], dtype=torch.float32)

# Task 3: Call the API
result = input_data.float(memory_format=torch.contiguous_format)