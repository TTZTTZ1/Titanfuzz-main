import torch
tensor1 = torch.tensor([1, 2, 3], dtype=torch.float32)
tensor2 = torch.tensor([1, 2, 4], dtype=torch.float32)
result = tensor1.ne(tensor2)
print(result)