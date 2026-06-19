import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
dim0 = 0
dim1 = 1
output_tensor = torch.transpose(input_tensor, dim0, dim1)
print(output_tensor)