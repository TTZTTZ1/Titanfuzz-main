import torch

a = torch.tensor([[1+1j, 2+2j], [3+3j, 4+4j]])
b = torch.tensor([[5+5j, 6+6j], [7+7j, 8+8j]])
result = torch.mul(a, b)
print(result)