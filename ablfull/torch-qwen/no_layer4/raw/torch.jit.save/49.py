import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

m = SimpleModel()
f = 'model.pt'
_extra_files = {'info.txt': 'Some info'}

torch.jit.save(m, f, _extra_files=_extra_files)