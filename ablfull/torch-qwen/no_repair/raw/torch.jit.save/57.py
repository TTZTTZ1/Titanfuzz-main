import torch

# Create a simple model to save
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

model = SimpleModel()

# Prepare valid input data
f = 'model.pt'

# Call the API
torch.jit.save(model, f)