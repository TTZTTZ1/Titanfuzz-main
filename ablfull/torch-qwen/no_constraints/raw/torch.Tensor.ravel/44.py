import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3)

# Task 3: Call the API
raveled_tensor = input_tensor.ravel()

print(raveled_tensor)