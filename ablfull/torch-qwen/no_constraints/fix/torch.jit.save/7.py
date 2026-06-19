import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)
model = SimpleModel()
dummy_input = torch.randn(1, 10)
traced_script_module = torch.jit.trace(model, dummy_input)
torch.jit.save(traced_script_module, 'simple_model.pt')