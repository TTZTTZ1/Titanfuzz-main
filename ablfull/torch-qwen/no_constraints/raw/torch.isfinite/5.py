import torch

# Task 2: Generate input data
input_data = torch.tensor([1.0, -float('inf'), float('nan'), 2.0])

# Task 3: Call the API
result = torch.isfinite(input_data)

print(result)