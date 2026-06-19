
import torch
input_tensor = torch.randn(2, 3, 4)
dim0 = 0
dim1 = 2
output_tensor = torch.transpose(input_tensor, dim0, dim1)
print(output_tensor)
