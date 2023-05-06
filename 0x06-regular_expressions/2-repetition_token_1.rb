#!/usr/bin/env ruby

sequence = /hb?t?n/
puts ARGV[0].scan(sequence).join
