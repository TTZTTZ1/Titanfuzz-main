import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
dummy_input = torch.randn(1, 10)
torch.jit.save(model, "simple_model.pt", _extra_files=None)