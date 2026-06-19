
import torch
script_module = torch.jit.script(torch.nn.Linear(10, 5))
torch.jit.save(script_module, 'model.pt')
