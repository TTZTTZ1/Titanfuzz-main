import torch

a = torch.tensor([[1+2j, 3+4j], [5+6j, 7+8j]])
b = torch.tensor([[1, 2], [3, 4]])
alpha = 2 + 3j
result = torch.sub(a, b, alpha=alpha)
print(result)