import torch

# Task 2: Generate input data
tensor = torch.tensor([1.0, 2.0, 3.0])

# Task 3: Call the API torch.Tensor.add_
result = tensor.add_(1.0)

print(result)