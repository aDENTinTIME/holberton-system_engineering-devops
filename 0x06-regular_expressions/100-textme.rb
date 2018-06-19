#!/usr/bin/env ruby
# An alternate shorter version with similar output \[(from|to|flags):([a-zA-Z0-9+:-]*)\]
puts ARGV[0].scan(/\[from:([a-zA-Z0-9+]*)\] \[to:([a-zA-Z0-9+]*)\] \[flags:([0-9:-]*)\]/).join(",")
