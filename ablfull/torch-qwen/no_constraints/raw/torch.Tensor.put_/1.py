import torch

# Task 2: Generate input data
indices = torch.tensor([0, 1, 2])
values = torch.tensor([10, 20, 30], dtype=torch.float32)
self = torch.zeros(5, dtype=torch.float32)

# Task 3: Call the API
self.put_(indices, values)
print(self)