import torch

# Task 2: Generate input data
x = torch.tensor([1.0], dtype=torch.float32)
y = torch.tensor([2.0], dtype=torch.float32)

# Task 3: Call the API
result = x.nextafter(y)
print(result)