import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, float('inf'), -float('inf'), 0.0])

# Task 3: Call the API torch.isfinite
result = torch.isfinite(input_data)
print(result)