import torch

# Task 2: Generate input data
m = torch.jit.script(torch.nn.Linear(10, 2))
f = 'model.pt'

# Task 3: Call the API
torch.jit.save(m, f)