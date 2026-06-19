import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mat1 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
mat2 = torch.tensor([[9.0, 10.0], [11.0, 12.0]])
result = torch.Tensor.addmm(input_tensor, mat1, mat2)
print(result)