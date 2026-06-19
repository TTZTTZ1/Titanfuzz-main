import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 2, 3], dtype=torch.float32)
tensor2 = torch.tensor([4, 2, 5], dtype=torch.float32)

# Task 3: Call the API
result = tensor1.ne(tensor2)
print(result)