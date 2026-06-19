import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 1, 4)

# Task 3: Call the API
output_tensor = input_tensor.squeeze_()
print(output_tensor)