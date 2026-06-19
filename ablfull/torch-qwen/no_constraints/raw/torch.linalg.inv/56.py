import torch

# Prepare input data: a square matrix of size 3x3 with non-zero determinant
input_data = torch.tensor([[4., 7., 2.], [6., 6., 18.], [-9., 0., 5.]])
result = torch.linalg.inv(input_data)
print(result)