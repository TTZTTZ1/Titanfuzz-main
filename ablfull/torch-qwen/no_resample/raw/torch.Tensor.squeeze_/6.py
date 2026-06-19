import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 2, 1)

# Task 3: Call the API
input_tensor.squeeze_(dim=0)
print(input_tensor)