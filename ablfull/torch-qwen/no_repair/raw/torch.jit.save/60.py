import torch

# Task 2: Generate input data
m = torch.jit.script(torch.nn.Linear(10, 5))  # Example ScriptModule
f = 'model.pt'  # File name for saving the model

# Task 3: Call the API torch.jit.save
torch.jit.save(m, f)