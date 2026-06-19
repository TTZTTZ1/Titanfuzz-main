import torch

# Task 2: Generate input data
input_tensor = torch.randn(5, 3)
p_norm = 2
max_norm = 1.0

# Task 3: Call the API torch.renorm
result = torch.renorm(input_tensor, p_norm, dim=0, max_norm=max_norm)

print(result)