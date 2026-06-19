import torch

# Task 2: Generate input data
tensor = torch.tensor([0, 0, 0], dtype=torch.int)
indices = torch.tensor([0, 2])
values = torch.tensor([99, -1])

# Task 3: Call the API
tensor.put_(indices, values)

print(tensor)