import torch

# Task 2: Generate input data
input1 = torch.randn(2, 3)
input2 = torch.randn(2, 4)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(3, 4), bias=None)