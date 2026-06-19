import torch

# Task 2: Generate input data
input1 = torch.randn(10, 5)
input2 = torch.randn(10, 3)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(5, 3), bias=None)