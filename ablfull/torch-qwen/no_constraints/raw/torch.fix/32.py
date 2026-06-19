import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-1.5, -0.3, 0.7, 1.2])

# Task 3: Call the API torch.fix
result = torch.fix(input_tensor)

print(result)