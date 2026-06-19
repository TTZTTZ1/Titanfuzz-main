import torch

# Task 2: Generate valid input data
input_data = torch.tensor([0.5, 0.7])

# Task 3: Call the API
result = input_data.bernoulli_()
print(result)