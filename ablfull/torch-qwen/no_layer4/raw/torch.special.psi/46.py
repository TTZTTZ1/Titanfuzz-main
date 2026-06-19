import torch

# Task 2: Generate input data
input_data = torch.tensor([-2.0, -1.5, 0.0, 1.0], dtype=torch.float32)

# Task 3: Call the API torch.special.psi
result = torch.special.psi(input_data)
print(result)