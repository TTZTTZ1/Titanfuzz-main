import torch
m = torch.jit.script(torch.nn.Linear(4, 4))
f = 'model.pt'
_extra_files = None
torch.jit.save(m, f, _extra_files=_extra_files)