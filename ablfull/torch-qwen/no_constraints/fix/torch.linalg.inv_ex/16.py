import torch
input_data = torch.tensor([[4.0, 7.0], [2.0, 6.0]])
result = torch.linalg.inv_ex(input_data)
print(result)