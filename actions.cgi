#!/usr/bin/perl

#########################################################################
#   Autori:             Marco Colombo (marco@openit.it)
#                       Giuliano Natali Diaolin (diaolin@openit.it)
#   Copyright:          Open It S.r.l.
#                       Viale Dante, 78
#                       38057 Pergine Valsugana (TN) ITALY
#                       Tel: +39 0461 534800 Fax: +39 0461 538443
##############################################################################

require './openvpn-lib.pl';

# legge parametri da form o da url e li inserisce in hash $in
&ReadParse();

if ($in{'action'} eq "start" and $config{'start_cmd'}) {
    $rv = &system_logged("$config{'start_cmd'} >/dev/null 2>&1 </dev/null");
    if ($rv) { &error(&text('start_fail', $config{'start_cmd'})); }
} elsif ($in{'action'} eq "stop" and $config{'stop_cmd'}) {
    $rv = &system_logged("$config{'stop_cmd'} >/dev/null 2>&1 </dev/null");
    if ($rv) { &error(&text('stop_fail', $config{'stop_cmd'})); }
} elsif ($in{'action'} eq "restart" and $config{'stop_cmd'} and $config{'start_cmd'}) {
    $rv = &system_logged("$config{'stop_cmd'} >/dev/null 2>&1 </dev/null");
    if ($rv) { &error(&text('stop_fail', $config{'stop_cmd'})); }
    $rv = &system_logged("$config{'start_cmd'} >/dev/null 2>&1 </dev/null");
    if ($rv) { &error(&text('start_fail', $config{'start_cmd'})); }
} else {
    &error(&text('cmdabsent'));
}

&redirect("index.cgi");