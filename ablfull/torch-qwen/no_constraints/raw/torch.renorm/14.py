import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)
p_norm = 2
dim = 1
maxnorm = 1.0

# Task 3: Call the API torch.renorm
result = torch.renorm(input_tensor, p_norm, dim, maxnorm)

print(result)