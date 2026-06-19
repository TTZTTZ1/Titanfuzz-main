import torch

# Task 2: Generate input data
m = torch.jit.script(torch.nn.Linear(5, 10))  # Example ScriptModule
f = "model.pt"

# Task 3: Call the API
torch.jit.save(m, f)