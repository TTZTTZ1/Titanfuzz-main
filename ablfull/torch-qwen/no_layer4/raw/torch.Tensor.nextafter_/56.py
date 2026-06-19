import torch

# Task 2: Generate input data
x = torch.tensor([1.0], dtype=torch.float32)
y = 2.0

# Task 3: Call the API
result = x.nextafter(y)