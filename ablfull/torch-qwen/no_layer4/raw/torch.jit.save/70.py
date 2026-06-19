import torch

# Task 2: Generate input data
script_module = torch.jit.script(torch.nn.Linear(10, 2))
file_path = "model.pt"

# Task 3: Call the API
torch.jit.save(script_module, file_path)