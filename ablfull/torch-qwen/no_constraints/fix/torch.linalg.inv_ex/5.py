import torch
input_matrix = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float32)
result = torch.linalg.inv_ex(input_matrix)
print(result)