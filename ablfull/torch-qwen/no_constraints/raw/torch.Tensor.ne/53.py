import torch

# Task 2: Generate input data
tensor1 = torch.tensor([1, 2, 3], dtype=torch.float32)
tensor2 = torch.tensor([1, 2, 4], dtype=torch.float32)

# Task 3: Call the API torch.Tensor.ne
result = tensor1.ne(tensor2)
print(result)