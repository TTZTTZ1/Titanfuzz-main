import torch

# Task 2: Generate input data
input_tensor = torch.randn(5, 5)

# Task 3: Call the API
result = torch.slogdet(input_tensor)
print(result)