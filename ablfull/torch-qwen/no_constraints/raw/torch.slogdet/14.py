import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4., 0.], [0., 3.]])

# Task 3: Call the API
result = torch.slogdet(input_tensor)

print(result)