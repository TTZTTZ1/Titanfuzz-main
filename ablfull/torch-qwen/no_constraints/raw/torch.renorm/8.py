import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)
p_norm = 2
dim = 1
max_norm = 1.0

# Task 3: Call the API
result = torch.renorm(input_tensor, p_norm, dim, max_norm)
print(result)