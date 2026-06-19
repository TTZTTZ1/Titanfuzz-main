import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Task 3: Call the API torch.Tensor.ravel
raveled_tensor = input_tensor.ravel()

print(raveled_tensor)