import torch

# Task 2: Generate input data
script_module = torch.jit.script(torch.nn.Linear(5, 3))
file_path = 'model.pt'
extra_files = {'metadata.txt': 'Some metadata'}

# Task 3: Call the API
torch.jit.save(script_module, file_path, _extra_files=extra_files)