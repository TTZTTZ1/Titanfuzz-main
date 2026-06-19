
import torch
tensor1 = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
tensor2 = torch.tensor([[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])
result = tensor1.cross(tensor2)
print(result)
