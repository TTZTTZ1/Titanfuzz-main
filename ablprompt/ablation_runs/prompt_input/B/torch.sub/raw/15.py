import torch

a = torch.tensor([[1+1j, 2+2j], [3+3j, 4+4j]])
b = torch.tensor([[1, 1], [1, 1]])
result = torch.sub(a, b, alpha=2)
print(result)