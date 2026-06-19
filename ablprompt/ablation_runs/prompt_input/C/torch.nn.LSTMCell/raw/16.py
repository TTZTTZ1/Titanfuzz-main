import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Input data (batch_size, input_size)
input_data = torch.randn(5, input_size)

# Initial hidden and cell states (batch_size, hidden_size)
h0 = torch.zeros(5, hidden_size)
c0 = torch.zeros(5, hidden_size)

# Process each time step
for i in range(input_data.size(0)):
    h0, c0 = lstm_cell(input_data[i], (h0, c0))

print("Final Hidden State:", h0)
print("Final Cell State:", c0)