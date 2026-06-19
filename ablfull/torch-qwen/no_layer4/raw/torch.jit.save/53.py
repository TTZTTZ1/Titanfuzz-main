import torch

# Create a simple PyTorch model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(5, 3)
    
    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
torch.jit.save(model, "simple_model.pt")