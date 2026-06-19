import torch

# Task 2: Generate input data
input1 = torch.randn(10, 3, 4)
input2 = torch.randn(10, 4, 5)

# Task 3: Call the API
output = torch.bmm(input1, input2)
print(output.shape)  # Should print torch.Size([10, 3, 5])