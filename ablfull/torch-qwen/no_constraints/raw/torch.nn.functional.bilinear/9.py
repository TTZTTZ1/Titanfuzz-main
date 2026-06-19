import torch

# Task 2: Generate input data
input1 = torch.randn(3, 4)
input2 = torch.randn(3, 5)

# Task 3: Call the API torch.nn.functional.bilinear
output = torch.nn.functional.bilinear(input1, input2, weight=torch.randn(4, 5))
print(output)