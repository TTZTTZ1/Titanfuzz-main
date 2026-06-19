import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-1.5, 0.3, 2.7])

# Task 3: Call the API torch.ceil
result = torch.ceil(input_tensor)

print(result)