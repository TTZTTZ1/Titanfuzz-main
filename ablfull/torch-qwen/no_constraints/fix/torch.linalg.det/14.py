import torch
matrix = torch.tensor([[4, 7], [2, 6]], dtype=torch.float32)
result = torch.linalg.det(matrix)
print(result)