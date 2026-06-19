import torch

# Task 2: Generate input data
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])

# Task 3: Call the API torch.cat
result = torch.cat((x, y), dim=0)
print(result)