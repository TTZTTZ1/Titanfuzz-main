import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[0, 1], [2, 0]])

# Task 3: Call the API torch.Tensor.nonzero
result = input_tensor.nonzero(as_tuple=True)
print(result)