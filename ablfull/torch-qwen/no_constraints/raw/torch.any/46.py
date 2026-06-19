import torch

# Task 2: Generate input data
input_tensor = torch.tensor([False, True, False])

# Task 3: Call the API torch.any
result = torch.any(input_tensor)

print(result)