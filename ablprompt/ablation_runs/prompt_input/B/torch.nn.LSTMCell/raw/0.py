import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Create random input data and initial hidden/cell states
input_data = torch.randn(num_time_steps, 1, input_size)
h_0 = torch.zeros(1, 1, hidden_size)
c_0 = torch.zeros(1, 1, hidden_size)

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Iterate over time steps and update hidden/cell states
for t in range(num_time_steps):
    h_0, c_0 = lstm_cell(input_data[t], (h_0, c_0))

print("Final Hidden State:", h_0)
print("Final Cell State:", c_0)