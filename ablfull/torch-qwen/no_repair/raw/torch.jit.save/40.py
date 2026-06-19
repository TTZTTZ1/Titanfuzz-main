import torch

# Create a simple script module
class MyModel(torch.nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.linear = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)

m = MyModel()
f = 'model.pt'
torch.jit.save(m, f)