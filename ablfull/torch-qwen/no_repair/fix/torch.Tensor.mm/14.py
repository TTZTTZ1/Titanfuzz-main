
import torch
tensor1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
tensor2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
assert (tensor1.shape[1] == tensor2.shape[0])
result = torch.Tensor.mm(tensor1, tensor2)
print(result)
