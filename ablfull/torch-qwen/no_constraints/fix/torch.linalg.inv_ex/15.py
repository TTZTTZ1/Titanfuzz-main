import torch
a = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float64)
result = torch.linalg.inv_ex(a)
print(result)