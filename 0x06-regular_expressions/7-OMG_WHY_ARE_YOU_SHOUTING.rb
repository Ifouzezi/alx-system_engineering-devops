#!/usr/bin/env ruby

sequence = /[A-Z]*/
puts ARGV[0].scan(sequence).join
