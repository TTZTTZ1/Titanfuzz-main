import torch

# Task 2: Generate input data
input1 = torch.tensor([1, 0, 1, 0], dtype=torch.uint8)
input2 = torch.tensor([1, 1, 0, 0], dtype=torch.uint8)

# Task 3: Call the API
result = torch.bitwise_or(input1, input2)
print(result)