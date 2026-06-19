import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)
model = SimpleModel()
dummy_input = torch.randn(1, 10)
traced_script_module = torch.jit.trace(model, dummy_input)
traced_script_module.save('simple_model.pt')