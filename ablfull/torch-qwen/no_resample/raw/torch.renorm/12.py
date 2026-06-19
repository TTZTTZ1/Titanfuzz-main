import torch

# Prepare input data
input_tensor = torch.tensor([[1.0, -2.0], [3.0, 4.0]])
p = 2.0
dim = 1
maxnorm = 5.0

# Call the API
result = torch.renorm(input_tensor, p, dim, maxnorm)
print(result)