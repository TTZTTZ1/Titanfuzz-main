import torch

# Task 2: Generate input data
tensors = [torch.tensor([1, 2]), torch.tensor([3, 4])]

# Task 3: Call the API
result = torch.cartesian_prod(*tensors)
print(result)