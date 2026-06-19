import torch

# Task 2: Generate input data - a tensor of shape (3,) filled with ones
input_tensor = torch.ones(3)

# Task 3: Call the API torch.Tensor.bernoulli_
result = input_tensor.bernoulli_()
print(result)