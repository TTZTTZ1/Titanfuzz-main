import torch

# Task 2: Generate input data
input_data = torch.tensor([[0, 1, 0], [2, 0, 3]])

# Task 3: Call the API torch.Tensor.nonzero
result = input_data.nonzero()
print(result)