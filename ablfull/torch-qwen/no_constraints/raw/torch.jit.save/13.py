import torch

# Task 2: Generate input data
m = torch.nn.Linear(10, 5)
f = 'model.pt'

# Task 3: Call the API
torch.jit.save(m, f)