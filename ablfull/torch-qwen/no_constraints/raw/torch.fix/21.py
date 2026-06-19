import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-1.5, -0.5, 0.5, 1.5])

# Task 3: Call the API
result = torch.fix(input_tensor)

print(result)