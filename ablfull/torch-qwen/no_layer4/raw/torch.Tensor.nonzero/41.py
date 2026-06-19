import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[0, 0], [0, 1]])

# Task 3: Call the API
result = input_tensor.nonzero(as_tuple=True)

print(result)