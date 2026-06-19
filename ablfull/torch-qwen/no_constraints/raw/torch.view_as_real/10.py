import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 4)

# Task 3: Call the API torch.view_as_real
result = torch.view_as_real(input_tensor)