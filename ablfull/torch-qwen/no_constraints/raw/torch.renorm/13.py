import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)
p_norm = 2
max_norm = 1.0

# Task 3: Call the API torch.renorm
result = torch.renorm(input_tensor, p=p_norm, dim=0, maxnorm=max_norm)

print(result)