import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
dummy_input = torch.randn(1, 10)
output_file = "simple_model.pt"

# Save the model
torch.jit.save(model, output_file, _extra_files=None)