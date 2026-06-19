import torch
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([1, 4, 3])
result = tensor1.ne(tensor2)
print(result)