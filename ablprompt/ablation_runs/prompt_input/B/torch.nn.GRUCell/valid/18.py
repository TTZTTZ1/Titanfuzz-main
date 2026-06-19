import torch
import torch.nn as nn

# Define the GRUCell
gru_cell = nn.GRUCell(input_size=10, hidden_size=20)

# Initialize hidden state
h0 = torch.zeros(1, 20)

# Input sequence
x = torch.randn(5, 1, 10)

# Process each time step
for t in range(x.size(0)):
    h0 = gru_cell(x[t], h0)

print(h0)