
import torch
script_module = torch.jit.script(torch.nn.Linear(5, 3))
file_path = 'model.pt'
torch.jit.save(script_module, file_path)
