import torch

# Task 2: Generate input data
indices = torch.tensor([0, 2])
values = torch.tensor([99, -99])
tensor = torch.zeros(4)

# Task 3: Call the API
tensor.put_(indices, values)
print(tensor)