import torch

# Task 2: Generate input data - a tensor within the range [-1, 1]
input_tensor = torch.tensor([0.5])

# Task 3: Call the API
result = torch.Tensor.arcsin_(input_tensor)

print(result)