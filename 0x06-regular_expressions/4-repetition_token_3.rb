#!/usr/bin/env ruby
# Function to find all occurrences of "hbt*n" in the input string
def find_hbts(input)
  input.scan(/hbt*n/)
end

# Extract the first argument from the command-line arguments
input_string = ARGV[0]

# Call the function to find occurrences and join them
puts find_hbts(input_string).join
