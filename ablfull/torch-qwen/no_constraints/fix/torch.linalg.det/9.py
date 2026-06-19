import torch
input_matrix = torch.tensor([[4, 7], [2, 6]], dtype=torch.float32)
result = torch.linalg.det(input_matrix)
print(result)