import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0])
other_value = torch.tensor([4.0, 5.0, 6.0])

# Task 3: Call the API
result = input_tensor.add_(other_value)