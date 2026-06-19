import torch

# Task 2: Generate input data
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()
input_data = torch.randn(1, 10)

# Task 3: Call the API
torch.jit.save(model, "simple_model.pt", _extra_files=None)