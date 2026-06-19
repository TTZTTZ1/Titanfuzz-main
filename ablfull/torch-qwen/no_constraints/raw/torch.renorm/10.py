import torch

# Task 2: Generate input data
x = torch.randn(3, 4)
p = 2
dim = 0
maxnorm = 1.5

# Task 3: Call the API
result = torch.renorm(x, p, dim, maxnorm)

print(result)