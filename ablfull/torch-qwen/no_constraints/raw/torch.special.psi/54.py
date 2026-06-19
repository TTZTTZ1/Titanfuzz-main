import torch

# Task 2: Generate input data
x = torch.tensor(0.5, requires_grad=True)

# Task 3: Call the API torch.special.psi
result = torch.special.psi(x)
print(result)