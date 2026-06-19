import torch

# Task 2: Generate input data
input_data = torch.randint(0, 10, (3, 4)).to(torch.float32)

# Task 3: Call the API
result = input_data.float(memory_format=torch.contiguous_format)