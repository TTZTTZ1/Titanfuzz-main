import torch

# Task 2: Generate input data
input_data = torch.randn(3, 4)

# Task 3: Call the API torch.Tensor.ravel
raveled_tensor = input_data.ravel()
print(raveled_tensor)