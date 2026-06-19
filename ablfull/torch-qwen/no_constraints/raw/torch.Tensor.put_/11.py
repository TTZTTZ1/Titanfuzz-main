import torch

# Task 2: Generate input data
tensor = torch.tensor([1, 2, 3])
index = torch.tensor([0, 2])
source = torch.tensor([9, 8])

# Task 3: Call the API
tensor.put_(index, source)
print(tensor)