import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[0, 0], [0, 1]], dtype=torch.bool)

# Task 3: Call the API torch.any
result = torch.any(input_tensor)
print(result)