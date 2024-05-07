#!/usr/bin/env ruby
# Check if there's exactly one argument provided
if ARGV.length == 1
  # Output all occurrences of "Holberton" in the input
  puts ARGV[0].scan(/School/).join
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

