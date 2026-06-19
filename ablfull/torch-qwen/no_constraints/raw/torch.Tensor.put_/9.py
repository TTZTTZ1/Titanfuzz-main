import torch

# Task 2: Generate input data
tensor = torch.tensor([1, 2, 3, 4])
index = torch.tensor([0, 2])
source = torch.tensor([99, 88])

# Task 3: Call the API torch.Tensor.put_
tensor.put_(index, source)
print(tensor)