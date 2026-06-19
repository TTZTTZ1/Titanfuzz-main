import torch

# Create a simple ScriptModule
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

m = MyModel()
f = 'my_model.pt'
torch.jit.save(m, f)