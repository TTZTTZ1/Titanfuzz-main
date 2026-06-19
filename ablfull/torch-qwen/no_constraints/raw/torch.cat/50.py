import torch

# Task 2: Generate input data
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])

# Task 3: Call the API torch.cat
result = torch.cat((a, b))

print(result)