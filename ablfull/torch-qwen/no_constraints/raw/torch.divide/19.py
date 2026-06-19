import torch

# Task 2: Generate input data
tensor1 = torch.tensor([4.0, 8.0], dtype=torch.float32)
tensor2 = torch.tensor([2.0, 4.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.divide(tensor1, tensor2)
print(result)