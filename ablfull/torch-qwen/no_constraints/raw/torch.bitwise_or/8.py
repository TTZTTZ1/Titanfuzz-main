import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 0, 1, 0], dtype=torch.uint8)
tensor2 = torch.tensor([0, 1, 0, 1], dtype=torch.uint8)

# Task 3: Call the API
result = torch.bitwise_or(tensor1, tensor2)
print(result)