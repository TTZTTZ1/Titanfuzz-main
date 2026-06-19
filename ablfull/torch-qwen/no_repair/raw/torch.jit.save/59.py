import torch

# Task 2: Generate input data
m = torch.jit.script(torch.nn.Linear(10, 5))  # ScriptModule example
f = "model.pt"  # File path string

# Task 3: Call the API
torch.jit.save(m, f)