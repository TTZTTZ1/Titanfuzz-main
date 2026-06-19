import torch

# Task 2: Generate input data
indices = torch.tensor([0, 2, 4])
values = torch.tensor([1.0, 2.0, 3.0])
tensor = torch.zeros(5)

# Task 3: Call the API
tensor.put_(indices, values)
print(tensor)