import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 2], dtype=torch.long)
tensor2 = torch.tensor([0.5, 0.75], dtype=torch.float)

# Task 3: Call the API
result = torch.cartesian_prod(tensor1, tensor2)
print(result)