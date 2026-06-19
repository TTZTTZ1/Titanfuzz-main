import torch

# Prepare valid input data
m = torch.jit.script(torch.nn.Linear(10, 5))  # Example model
f = 'model.pt'  # File path to save the model
_extra_files = {'metadata.txt': 'Some metadata'}  # Optional extra files

# Call the API
torch.jit.save(m, f, _extra_files=_extra_files)