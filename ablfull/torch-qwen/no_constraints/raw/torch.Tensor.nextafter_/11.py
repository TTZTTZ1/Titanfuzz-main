import torch

# Task 2: Generate input data
x = torch.tensor(0.5)
y = torch.tensor(0.6)

# Task 3: Call the API
result = x.nextafter(y)

print(result)