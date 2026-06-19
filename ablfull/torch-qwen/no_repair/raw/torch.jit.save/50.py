import torch

# Step 2: Generate input data
script_module = torch.jit.script(torch.nn.Linear(10, 5))
file_path = 'model.pt'

# Step 3: Call the API
torch.jit.save(script_module, file_path)