import torch

# Task 2: Generate input data
batch_size = 2
mat1 = torch.randn(batch_size, 3, 4)
mat2 = torch.randn(batch_size, 4, 5)

# Task 3: Call the API torch.bmm
result = torch.bmm(mat1, mat2)
print(result)