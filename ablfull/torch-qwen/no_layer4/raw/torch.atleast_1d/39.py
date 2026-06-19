import torch

# Task 2: Generate input data
input_tensor = torch.tensor(5)

# Task 3: Call the API torch.atleast_1d
result = torch.atleast_1d(input_tensor)

print(result)