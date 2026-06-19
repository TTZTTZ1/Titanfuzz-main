import torch

# Task 2: Generate input data
n = 4
input_tensor = torch.randn(n, n)

# Task 3: Call the API
result = torch.slogdet(input_tensor)
print(result)