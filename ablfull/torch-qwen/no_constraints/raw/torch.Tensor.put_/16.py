import torch

# Task 2: Generate input data
indices = torch.tensor([0, 1, 2])
values = torch.tensor([10, 20, 30])

# Task 3: Call the API
tensor = torch.zeros(5)
tensor.put_(indices, values)

print(tensor)