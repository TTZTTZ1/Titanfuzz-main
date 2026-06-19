import torch
A = torch.tensor([[4.0, (- 2.0)], [1.0, 1.0]])
result = torch.slogdet(A)
print(result)