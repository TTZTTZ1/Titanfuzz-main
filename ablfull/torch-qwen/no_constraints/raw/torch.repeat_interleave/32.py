import torch

# Task 2: Generate input data
tensor = torch.tensor([[1, 2], [3, 4]])
repeats = 3

# Task 3: Call the API
result = torch.repeat_interleave(tensor, repeats)

print(result)