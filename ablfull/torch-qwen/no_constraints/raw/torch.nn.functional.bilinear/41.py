import torch

# Task 2: Generate input data
input1 = torch.randn(4, 5)
input2 = torch.randn(4, 6)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(5, 6), bias=None)