import torch
input_data = torch.tensor([[4, 7], [2, 6]], dtype=torch.float32)
result = torch.linalg.det(input_data)
print(result)