import torch

# Prepare valid input data
input1 = torch.randn(10)
input2 = torch.randn(10)
weight1 = torch.randn(5, 10)
weight2 = torch.randn(5, 10)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, weight1, weight2)