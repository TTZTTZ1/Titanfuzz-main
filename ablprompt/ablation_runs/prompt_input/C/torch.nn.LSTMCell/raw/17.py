import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Initialize input data and hidden/cell states
input_data = torch.randn(num_time_steps, 1, input_size)
h0 = torch.zeros(1, 1, hidden_size)
c0 = torch.zeros(1, 1, hidden_size)

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Iterate over each time step and update the hidden and cell states
for t in range(num_time_steps):
    h0, c0 = lstm_cell(input_data[t], (h0, c0))

# Output the final hidden state
print("Final Hidden State:", h0)