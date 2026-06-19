import torch

# Task 2: Generate input data
n = 4
input_data = torch.randn(n, n)

# Task 3: Call the API
result = torch.slogdet(input_data)
print(result)