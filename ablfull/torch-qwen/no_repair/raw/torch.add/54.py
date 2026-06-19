import torch

# Task 2: Generate input data
input_tensor = torch.tensor([1, 2, 3], dtype=torch.float)
other_tensor = torch.tensor([4, 5, 6], dtype=torch.float)

# Task 3: Call the API torch.add
result = torch.add(input_tensor, other_tensor, alpha=0.5)
print(result)