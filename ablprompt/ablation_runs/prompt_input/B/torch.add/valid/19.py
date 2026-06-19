import torch

a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
c = torch.tensor([[0.5, 0.5], [0.5, 0.5]], dtype=torch.float32)

result = torch.add(a, b, alpha=2, out=c)
print(result)