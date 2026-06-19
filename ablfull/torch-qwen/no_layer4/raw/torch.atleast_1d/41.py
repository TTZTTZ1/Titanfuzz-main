import torch

# Task 2: Generate input data
input_data = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]

# Task 3: Call the API
result = torch.atleast_1d(*input_data)
print(result)