import torch
m = torch.jit.script(torch.nn.Linear(10, 5))
f = 'model.pt'
_extra_files = {}
torch.jit.save(m, f, _extra_files=_extra_files)