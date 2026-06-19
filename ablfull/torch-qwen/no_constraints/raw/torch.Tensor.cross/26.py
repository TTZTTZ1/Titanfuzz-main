import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 0, 0], dtype=torch.float32)
tensor2 = torch.tensor([0, 1, 0], dtype=torch.float32)

# Task 3: Call the API torch.Tensor.cross
result = tensor1.cross(tensor2)

print(result)