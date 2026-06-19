import torch

# Task 2: Generate input data
input_tensor = torch.rand(5)

# Task 3: Call the API
result = input_tensor.bernoulli_()
print(result)