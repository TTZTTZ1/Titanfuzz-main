import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 2)

# Task 3: Call the API
input_tensor.squeeze_()
print(input_tensor)