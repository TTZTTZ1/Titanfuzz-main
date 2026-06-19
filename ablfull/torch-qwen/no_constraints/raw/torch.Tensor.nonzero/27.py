import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[0, 1, 0], [2, 0, 3]])

# Task 3: Call the API
result = input_tensor.nonzero()
print(result)