import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([1, 0, 3])

# Task 3: Call the API
result = tensor1.ne(tensor2)

print(result)