import torch

# Task 2: Generate input data
a = torch.tensor([1.0, 2.0], dtype=torch.float32)
b = torch.tensor([1.5, 2.5], dtype=torch.float32)

# Task 3: Call the API
result = a.nextafter(b)
print(result)