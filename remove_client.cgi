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

&ReadVPNConf();
&ReadClientConf();
$in{'CLIENT_NAME'} = $in{'client'};
&ReadFieldsCA($in{'CA_NAME'});
$in{'ca_name'} = $in{'CA_NAME'};
$in{'key_name'} = $in{'CLIENT_NAME'};

# intestazione pagina
&ui_print_header(undef, $text{'title_opnvpn'}, "", "intro", 1, 1, undef,
                &help_search_link("openvpn", "man", "doc", "google")."<a href=\"index.cgi\">".$text{'title_opnvpn'}."</a>",
                undef, undef, &text('index_openvpn')." ".&text('version')." ".$config{'openvpn_version'}.", ".&text('index_openssl')." ".&text('version')." ".$config{'openssl_version'});

print "<BR>";

&remove_client($in{'client'},$in{'vpn'});

print "<table border width=100%>\n";
print "<tr bgcolor=red><td nowrap><b>".$in{'CLIENT_NAME'}.': '.$text{'client_removed'}."</b></td></tr>\n";
print "</table>\n";

print "<BR><BR>";

#footer della pagina
&footer("clientlist_vpn.cgi?vpn=".$in{'vpn'}, $text{'list_client_vpn'}." ".$in{'vpn'});
