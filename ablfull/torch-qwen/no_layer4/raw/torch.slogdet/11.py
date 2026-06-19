import torch

# Task 2: Generate input data
input_data = torch.randn(4, 4)

# Task 3: Call the API
result = torch.slogdet(input_data)
print(result)