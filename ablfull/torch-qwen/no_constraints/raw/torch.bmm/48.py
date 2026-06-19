import torch

# Task 2: Generate input data
input1 = torch.randn(2, 3, 4)
input2 = torch.randn(2, 4, 5)

# Task 3: Call the API
result = torch.bmm(input1, input2)