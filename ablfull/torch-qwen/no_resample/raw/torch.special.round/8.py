import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1.5, -2.3, 4.8], dtype=torch.float)

# Task 3: Call the API
result = torch.special.round(input_tensor)
print(result)