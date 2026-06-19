import torch
script_module = torch.jit.script(torch.nn.Linear(10, 5))
file_path = 'model.pt'
torch.jit.save(script_module, file_path)