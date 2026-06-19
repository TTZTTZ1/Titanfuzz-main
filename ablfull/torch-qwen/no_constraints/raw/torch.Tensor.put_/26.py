import torch

# Task 2: Generate input data
tensor = torch.tensor([0, 1, 2, 3])
indices = torch.tensor([0, 2])
values = torch.tensor([99, 88])

# Task 3: Call the API torch.Tensor.put_
tensor.put_(indices, values)
print(tensor)