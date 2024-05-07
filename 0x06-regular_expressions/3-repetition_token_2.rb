#!/usr/bin/env ruby
# Check if there's exactly one argument provided
if ARGV.length == 1
  # Match "hbt" followed by one or more occurrences of "t" and then "n"
  matches = ARGV[0].scan(/hbt+n/)
  
  # Output all matches
  puts matches.join
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end
