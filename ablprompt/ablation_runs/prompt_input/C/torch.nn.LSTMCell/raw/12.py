import torch
import torch.nn as nn

# Define the LSTMCell
input_size = 10
hidden_size = 20
lstm_cell = nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(5, input_size)  # 5 timesteps, each of size input_size
hx = torch.zeros(5, hidden_size)
cx = torch.zeros(5, hidden_size)

# Process each timestep
for i in range(input_data.size(0)):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

print(hx)