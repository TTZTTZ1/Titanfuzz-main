import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API
output_tensor = input_tensor.double(memory_format=torch.preserve_format)