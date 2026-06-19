import torch
tensor = torch.tensor([1, 2, 3])
result = torch.atleast_1d(tensor)
tensor1 = torch.tensor([4, 5])
tensor2 = torch.tensor([6, 7])
result_sequence = torch.atleast_1d(tensor1, tensor2)