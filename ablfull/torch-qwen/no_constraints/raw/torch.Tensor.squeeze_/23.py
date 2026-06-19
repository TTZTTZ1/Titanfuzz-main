import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 2, 2)

# Task 3: Call the API
result_tensor = input_tensor.squeeze_()
print(result_tensor)