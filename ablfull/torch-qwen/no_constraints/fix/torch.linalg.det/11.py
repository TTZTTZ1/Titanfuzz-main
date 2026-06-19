import torch
tensor = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
result = torch.linalg.det(tensor)
print(result)