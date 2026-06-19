import torch
matrix = torch.randint((- 10), 11, (5, 5), dtype=torch.float32)
result = torch.linalg.det(matrix)