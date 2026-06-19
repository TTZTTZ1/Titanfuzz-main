import torch

# Task 2: Generate input data
input1 = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
input2 = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float32)

# Task 3: Call the API torch.add
result = torch.add(input1, input2)
print(result)