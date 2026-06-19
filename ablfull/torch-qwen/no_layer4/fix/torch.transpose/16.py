import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
dim0 = 0
dim1 = 1
result = torch.transpose(input_tensor, dim0, dim1)
print(result)