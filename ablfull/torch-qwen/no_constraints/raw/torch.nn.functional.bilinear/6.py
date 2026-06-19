import torch

# Task 2: Generate input data
input1 = torch.randn(5)
input2 = torch.randn(5)
weight = torch.randn(5, 5)

# Task 3: Call the API
output = torch.nn.functional.bilinear(input1, input2, weight)