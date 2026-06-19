import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3])
repeats = [2, 3, 4]

# Task 3: Call the API
result = torch.repeat_interleave(input_tensor, repeats)

print(result)