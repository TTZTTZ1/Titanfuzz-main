import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[False, False], [True, True]])

# Task 3: Call the API
result = torch.any(input_tensor)
print(result)