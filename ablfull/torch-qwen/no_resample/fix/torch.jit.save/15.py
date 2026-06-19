import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)
model = SimpleModel()
traced_model = torch.jit.trace(model, torch.randn(1, 10))
torch.jit.save(traced_model, 'model.pt')