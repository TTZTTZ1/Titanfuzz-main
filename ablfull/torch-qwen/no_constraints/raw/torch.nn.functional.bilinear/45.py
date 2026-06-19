import torch

# Generate input data
input1 = torch.randn(3, 5)
input2 = torch.randn(3, 6)

# Call the API
output = torch.nn.functional.bilinear(input1, input2, None)