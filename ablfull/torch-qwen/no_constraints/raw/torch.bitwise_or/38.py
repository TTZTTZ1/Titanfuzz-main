import torch

# Task 2: Generate input data
input_tensor1 = torch.tensor([0b1100], dtype=torch.uint8)
input_tensor2 = torch.tensor([0b1010], dtype=torch.uint8)

# Task 3: Call the API torch.bitwise_or
result = torch.bitwise_or(input_tensor1, input_tensor2)