import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API torch.Tensor.double
result = input_data.double(memory_format=torch.preserve_format)