import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[0.5, 0.7], [0.3, 0.9]])

# Task 3: Call the API
result_tensor = input_tensor.bernoulli_()

print(result_tensor)