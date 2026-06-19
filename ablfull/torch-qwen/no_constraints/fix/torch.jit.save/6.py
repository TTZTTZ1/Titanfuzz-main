import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)
model = SimpleModel()
input_data = torch.randn(1, 10)
output_file = 'model.pt'
torch.jit.trace(model, input_data).save(output_file)