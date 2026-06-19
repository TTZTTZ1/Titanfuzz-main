import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-1.0, 2.0, -3.0])
sign_tensor = torch.tensor([1.0, -1.0, 1.0])

# Task 3: Call the API
result_tensor = input_tensor.copysign_(sign_tensor)