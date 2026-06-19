import torch

# Task 2: Generate input data
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Task 3: Call the API torch.cat
result = torch.cat((a, b))
print(result)