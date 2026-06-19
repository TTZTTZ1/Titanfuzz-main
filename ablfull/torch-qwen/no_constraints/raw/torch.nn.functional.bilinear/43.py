import torch

# Task 2: Generate input data
input1 = torch.randn(4)
input2 = torch.randn(4)
weight = torch.randn(4, 2)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)