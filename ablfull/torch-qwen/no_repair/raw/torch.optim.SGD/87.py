import torch

model = torch.nn.Linear(3, 4)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)