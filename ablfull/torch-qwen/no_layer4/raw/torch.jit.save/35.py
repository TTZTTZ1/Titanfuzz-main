import torch

# Create a simple script module
class MyModule(torch.nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

m = MyModule()
f = 'model.pt'
torch.jit.save(m, f)