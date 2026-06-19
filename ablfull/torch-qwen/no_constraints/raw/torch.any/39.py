import torch

# Task 2: Generate input data
input_data = torch.tensor([False, False, True])

# Task 3: Call the API
result = torch.any(input_data)
print(result)