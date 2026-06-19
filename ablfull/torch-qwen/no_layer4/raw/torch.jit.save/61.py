import torch

# Prepare valid input data
m = torch.jit.script(torch.nn.Linear(4, 4))
f = 'model.pt'
_extra_files = None

# Call the target API
torch.jit.save(m, f, _extra_files=_extra_files)