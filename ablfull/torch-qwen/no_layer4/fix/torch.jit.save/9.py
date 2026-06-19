import torch
script_module = torch.jit.script(torch.nn.Linear(10, 2))
file_path = 'model.pt'
torch.jit.save(script_module, file_path)