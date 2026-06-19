import torch

# Generate input data
input1 = torch.randn(2, 5)
input2 = torch.randn(3, 5)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(2, 3, 5), bias=None)