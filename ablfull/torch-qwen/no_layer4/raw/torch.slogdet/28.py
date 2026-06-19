import torch

# Task 2: Generate input data
input_data = torch.randn(3, 3)

# Task 3: Call the API
result = torch.slogdet(input_data)
print(result)