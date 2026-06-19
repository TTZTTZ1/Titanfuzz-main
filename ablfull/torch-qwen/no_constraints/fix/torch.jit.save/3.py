import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)
model = SimpleModel()
scripted_model = torch.jit.script(model)
input_data = torch.randn(1, 10)
torch.jit.save(scripted_model, 'model.pt')