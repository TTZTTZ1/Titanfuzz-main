import torch
tensor1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
tensor2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
result = tensor1.mm(tensor2)