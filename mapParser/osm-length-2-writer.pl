#!/usr/bin/perl
use strict;
# This script was modified by Marcos Tomaszewski<marcos.tomaszewski@grad.ufsc.br>
# to suit better on the Map Parser of the Road Network Optimizer Project
# Changes:
# -This version writes it output to a file named length_a.osm
# where "a" is the original input file
# -The script dont print the sum of the lengths in any way
# since the purpose is just calcule the individual way length


# Script that computes lengths of ways in an OSM file.
#
# Reads the OSM file on stdin.
# Writes an OSM file to stdout in which all ways carry an additional
# tag: <d length="1234.567">, specifying the length in metres.
#
# On stderr, outputs a list of all highway types encountered together 
# with total length.
#
# Stores all node positions in a memory hash and will thus be unable
# to process the whole planet file unlesss you have 8 Gig of RAM or so.
#
# Author: Frederik Ramm <frederik@remote.org>. My contribution is 
# Public Domain but I grabbed the Haversine formula in calc_distance 
# from the original osm-length script, written by Jochen Topf, which
# is GPL, so the whole of this script is GPL also - if you need a
# true PD variant, re-implement the Haversine yourself.

my $nodes = {};

use constant PI => 4 * atan2 1, 1;
use constant DEGRAD => PI / 180;
use constant RADIUS => 6367000.0;

my $waylen;
my $hw;
my $warning;
my $lastnode;
my $line;
#$ARGV[0] param 1


my $output_file =  substr $ARGV[0], 0, -4;
$output_file = $output_file . '_length.osm';
open(my $fh, '>', $output_file) or die "Could not open file $!";

while(<>) 
{
    if (/^\s*<node.*\sid=["']([0-9-]+)['"].*lat=["']([0-9.-]+)["'].*lon=["']([0-9.-]+)["']/)
    {
        $nodes->{$1}=[$2,$3];
    }
    elsif (/^\s*<way /)
    {
        $waylen = 0;
        undef $hw;
        undef $warning;
        undef $lastnode;
    }
    elsif (defined($waylen) && /k=.highway.\s*v=["'](.*?)["']/)
    {
        $hw = $1;
    }
    elsif (/^\s*<nd ref=['"](.*)["']/)
    {
        if (defined($nodes->{$1}) && defined($lastnode))
        {
            $waylen += calc_distance($lastnode, $nodes->{$1});
        }
        $lastnode = $nodes->{$1};
    }
    elsif (defined($hw) && (/^\s*<\/way/))
    {
        print $fh "   <d length='" . $waylen . "'/>\n";
    }
    print $fh $_;
}

# printf STDERR  "done\n";
close $fh;

sub calc_distance {
    my ($p1, $p2) = @_;

    my ($lat1, $lon1, $lat2, $lon2) = ($p1->[0] * DEGRAD, $p1->[1] * DEGRAD, $p2->[0] * DEGRAD, $p2->[1] * DEGRAD);

    my $dlon = ($lon2 - $lon1);
    my $dlat = ($lat2 - $lat1);
    my $a = (sin($dlat/2))**2 + cos($lat1) * cos($lat2) * (sin($dlon/2))**2;
    my $c = 2 * atan2(sqrt($a), sqrt(1-$a)) ;
    return RADIUS * $c;
}
