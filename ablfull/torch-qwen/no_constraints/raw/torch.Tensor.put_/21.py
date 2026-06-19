import torch

# Task 2: Generate input data
indices = torch.tensor([0, 1, 2])
values = torch.tensor([4, 5, 6], dtype=torch.float32)
tensor = torch.zeros(3)

# Task 3: Call the API torch.Tensor.put_
tensor.put_(indices, values)
print(tensor)