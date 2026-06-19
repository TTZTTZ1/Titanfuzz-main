import torch

# Prepare valid input data
model = torch.jit.script(torch.nn.Linear(10, 5))
file_path = 'model.pt'

# Call the API
torch.jit.save(model, file_path)