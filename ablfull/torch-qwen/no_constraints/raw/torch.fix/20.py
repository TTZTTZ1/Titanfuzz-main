import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-1.5, 0.0, 1.5], dtype=torch.float32)

# Task 3: Call the API torch.fix
result = torch.fix(input_tensor)
print(result)