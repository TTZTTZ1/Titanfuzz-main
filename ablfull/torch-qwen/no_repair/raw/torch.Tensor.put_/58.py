import torch

# Task 2: Generate input data
index = torch.tensor([0, 1, 2], dtype=torch.int)
source = torch.tensor([3, 4, 5], dtype=torch.float)

# Task 3: Call the API
result = torch.Tensor([6, 7, 8, 9]).put_(index, source, accumulate=True)

print(result)