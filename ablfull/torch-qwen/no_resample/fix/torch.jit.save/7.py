import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)
model = SimpleModel()
f = 'simple_model.pt'
torch.jit.trace(model, torch.randn(1, 10)).save(f)