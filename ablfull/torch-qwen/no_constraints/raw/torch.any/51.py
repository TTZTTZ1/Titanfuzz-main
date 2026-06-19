import torch

# Task 2: Generate input data - a tensor with True values
input_tensor = torch.tensor([[True, False], [False, True]])

# Task 3: Call the API torch.any
result = torch.any(input_tensor)
print(result)