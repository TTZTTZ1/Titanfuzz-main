import torch

# Task 2: Generate input data
input1 = torch.randn(5, 10)
input2 = torch.randn(5, 20)
weight = torch.randn(10, 20)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)