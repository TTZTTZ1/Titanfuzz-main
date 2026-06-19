import torch

# Task 2: Generate input data
tensor = torch.tensor([[1, 2], [3, 4]])
split_size_or_sections = 2
dim = 0

# Task 3: Call the API torch.Tensor.split
result = tensor.split(split_size_or_sections, dim)
print(result)