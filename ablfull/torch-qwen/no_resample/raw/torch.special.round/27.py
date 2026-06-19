import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.5, -2.3, 0.7])

# Task 3: Call the API torch.special.round
result = torch.special.round(input_tensor)
print(result)