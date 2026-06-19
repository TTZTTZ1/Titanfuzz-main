import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden states
input_data = torch.randn(num_time_steps, input_size)
hx = torch.zeros(1, hidden_size)
cx = torch.zeros(1, hidden_size)

# Process each time step
for i in range(num_time_steps):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

print("Final hidden state:", hx)
print("Final cell state:", cx)