import torch
tensor1 = torch.tensor([1, 0, 0], dtype=torch.float32)
tensor2 = torch.tensor([0, 1, 0], dtype=torch.float32)
result = tensor1.cross(tensor2)
print(result)