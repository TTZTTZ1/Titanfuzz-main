import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0], dtype=torch.float32)
other_value = torch.tensor([2.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.nextafter(input_tensor, other_value)