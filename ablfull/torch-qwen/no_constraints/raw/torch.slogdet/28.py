import torch

# Task 2: Generate input data
input_matrix = torch.tensor([[4., 7.], [2., 6.]])

# Task 3: Call the API torch.slogdet
result = torch.slogdet(input_matrix)

print(result)