import torch

# Task 2: Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([9, 8, 7])

# Task 3: Call the API
result = torch.Tensor(5).put_(index, source)
print(result)