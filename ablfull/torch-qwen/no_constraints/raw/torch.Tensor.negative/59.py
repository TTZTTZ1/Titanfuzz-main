import torch

# Task 2: Generate input data - create a tensor of random floats between 0 and 1
input_data = torch.rand(3, requires_grad=True)

# Task 3: Call the API torch.Tensor.negative
result = input_data.negative()