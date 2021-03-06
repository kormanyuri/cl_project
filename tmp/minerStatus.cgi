<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="cache-control" content="no-cache" />
<link rel="stylesheet" type="text/css" media="screen" href="/css/cascade.css" />
<!--[if IE 6]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie6.css" /><![endif]-->
<!--[if IE 7]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie7.css" /><![endif]-->
<!--[if IE 8]><link rel="stylesheet" type="text/css" media="screen" href="/css/ie8.css" /><![endif]-->
<script type="text/javascript" src="/js/xhr.js"></script>
<script type="text/javascript" src="/js/jquery-1.10.2.js"></script>
<script type="text/javascript" src="/js/json2.min.js"></script>
<title>Ant Miner</title>
</head>
<body class="lang_en">
<p class="skiplink">
<span id="skiplink1"><a href="#navigation">Skip to navigation</a></span>
<span id="skiplink2"><a href="#content">Skip to content</a></span>
</p>
<div id="menubar">
<h2 class="navigation"><a id="navigation" name="navigation">Navigation</a></h2>
<div class="clear"></div>
</div>
<div id="menubar" style="background-color: #0a2b40;">
<div class="hostinfo" style="float: left; with: 500px;">
<img src="/images/antminer_logo.png" width="92" height="50" alt="" title="" border="0" />
</div>
<div class="clear"></div>
</div>
<div id="maincontainer">
<div id="tabmenu">
<div class="tabmenu1">
<ul class="tabmenu l1">
<li class="tabmenu-item-status"><a href="/index.html">System</a></li>
<li class="tabmenu-item-system"><a href="/cgi-bin/minerConfiguration.cgi">Miner Configuration</a></li>
<li class="tabmenu-item-network active"><a href="/cgi-bin/minerStatus.cgi">Miner Status</a></li>
<li class="tabmenu-item-system"><a href="/network.html">Network</a></li>
</ul>
<br style="clear: both" />
</div>
</div>
<div id="maincontent">
<noscript>
<div class="errorbox">
<strong>Java Script required!</strong><br /> You must enable Java Script in your browser or LuCI will not work properly.
</div>
</noscript>
<h2 style="padding-bottom:10px;"><a id="content" name="content">Miner Status</a></h2>
<div class="cbi-map" id="cbi-bmminerstatus">
<!-- tblsection -->
<fieldset class="cbi-section" id="cbi-table-table">
<legend>Summary</legend>
<div class="cbi-section-descr"></div>
<div class="cbi-section-node">
<table class="cbi-section-table">
<tr class="cbi-section-table-titles">
<th class="cbi-section-table-cell">Elapsed</th>
<th class="cbi-section-table-cell">GH/S(RT)</th>
<th class="cbi-section-table-cell">GH/S(avg)</th>
<th class="cbi-section-table-cell">FoundBlocks</th>
<th class="cbi-section-table-cell">LocalWork</th>								
<th class="cbi-section-table-cell">Utility</th>

<th class="cbi-section-table-cell">WU</th>
<th class="cbi-section-table-cell">BestShare</th>
</tr>
<tr class="cbi-section-table-descr">
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
</tr>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="ant_elapsed">13m14s</div>
<div id="cbip-table-1-elapsed"></div>
</td>
<td class="cbi-value-field">
<div id="ant_ghs5s">4,768.336</div>
<div id="cbip-table-1-ghs5s"></div>
</td>
<td class="cbi-value-field">
<div id="ant_ghsav">4,781.69</div>
<div id="cbip-table-1-ghsav"></div>
</td>
<td class="cbi-value-field">
<div id="ant_foundblocks">0</div>
<div id="cbip-table-1-foundblocks"></div>
</td>
<td class="cbi-value-field">
<div id="ant_localwork">6,578</div>
<div id="cbip-table-1-localwork"></div>
</td>
<td class="cbi-value-field">
<div id="ant_utility">0.53</div>
<div id="cbip-table-1-utility"></div>
</td>
<td class="cbi-value-field">
<div id="ant_wu">34,666.40</div>
<div id="cbip-table-1-wu"></div>
</td>
<td class="cbi-value-field">
<div id="ant_bestshare">333861</div>
<div id="cbip-table-1-bestshare"></div>
</td>
</tr>
</table>
</div>
</fieldset>
<!-- /tblsection -->
<!-- tblsection -->
<fieldset class="cbi-section" id="cbi-table-table">
<legend>Pools</legend>
<div class="cbi-section-descr"></div>
<div class="cbi-section-node">
<table id="ant_pools" class="cbi-section-table">
<tr class="cbi-section-table-titles">
<th class="cbi-section-table-cell">Pool</th>
<th class="cbi-section-table-cell">URL</th>
<th class="cbi-section-table-cell">User</th>
<th class="cbi-section-table-cell">Status</th>
                                                                 <th class="cbi-section-table-cell">Diff</th>
                                                                 <th class="cbi-section-table-cell">GetWorks</th>
                                                                 <th class="cbi-section-table-cell">Priority</th>
 <th class="cbi-section-table-cell">Accepted</th>		
                                                                 <th class="cbi-section-table-cell">Diff1#</th>
 	 <th class="cbi-section-table-cell">DiffA#</th>
 <th class="cbi-section-table-cell">DiffR#</th>
 <th class="cbi-section-table-cell">DiffS#</th>						         	
<th class="cbi-section-table-cell">Rejected</th>
<th class="cbi-section-table-cell">Discarded</th>
<th class="cbi-section-table-cell">Stale</th>
<th class="cbi-section-table-cell">LSDiff</th>
<th class="cbi-section-table-cell">LSTime</th>
</tr>
<tr class="cbi-section-table-descr">
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
</tr>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-pool">0</div>
<div id="cbip-table-1-pool"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-url">stratum+tcp://stratum.antpool.com:3333</div>
<div id="cbip-table-1-url"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-user">antminer_1</div>
<div id="cbip-table-1-user"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status">Alive</div>
<div id="cbip-table-1-status"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff">65.5K</div>
<div id="cbip-table-1-diff"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-getworks">24</div>
<div id="cbip-table-1-getworks"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-priority">0</div>
<div id="cbip-table-1-priority"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-accepted">7</div>
<div id="cbip-table-1-accepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff1shares">0</div>
<div id="cbip-table-1-diff1shares"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffaccepted">458,752</div>
<div id="cbip-table-1-diffaccepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffrejected">0</div>
<div id="cbip-table-1-diffrejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffstale">0</div>
<div id="cbip-table-1-diffstale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rejected">0</div>
<div id="cbip-table-1-rejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-discarded">411</div>
<div id="cbip-table-1-discarded"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-stale">0</div>
<div id="cbip-table-1-stale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharedifficulty">65,536</div>
<div id="cbip-table-1-lastsharedifficulty"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharetime">0:00:11</div>
<div id="cbip-table-1-lastsharetime"></div>
</td>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-pool">1</div>
<div id="cbip-table-1-pool"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-url">stratum+tcp://stratum.antpool.com:443</div>
<div id="cbip-table-1-url"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-user">antminer_1</div>
<div id="cbip-table-1-user"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status">Alive</div>
<div id="cbip-table-1-status"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff"></div>
<div id="cbip-table-1-diff"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-getworks">2</div>
<div id="cbip-table-1-getworks"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-priority">1</div>
<div id="cbip-table-1-priority"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-accepted">0</div>
<div id="cbip-table-1-accepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff1shares">0</div>
<div id="cbip-table-1-diff1shares"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffaccepted">0</div>
<div id="cbip-table-1-diffaccepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffrejected">0</div>
<div id="cbip-table-1-diffrejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffstale">0</div>
<div id="cbip-table-1-diffstale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rejected">0</div>
<div id="cbip-table-1-rejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-discarded">0</div>
<div id="cbip-table-1-discarded"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-stale">0</div>
<div id="cbip-table-1-stale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharedifficulty">0</div>
<div id="cbip-table-1-lastsharedifficulty"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharetime">Never</div>
<div id="cbip-table-1-lastsharetime"></div>
</td>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-pool">2</div>
<div id="cbip-table-1-pool"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-url">stratum+tcp://stratum.antpool.com:25</div>
<div id="cbip-table-1-url"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-user">antminer_1</div>
<div id="cbip-table-1-user"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status">Alive</div>
<div id="cbip-table-1-status"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff"></div>
<div id="cbip-table-1-diff"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-getworks">2</div>
<div id="cbip-table-1-getworks"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-priority">2</div>
<div id="cbip-table-1-priority"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-accepted">0</div>
<div id="cbip-table-1-accepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff1shares">0</div>
<div id="cbip-table-1-diff1shares"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffaccepted">0</div>
<div id="cbip-table-1-diffaccepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffrejected">0</div>
<div id="cbip-table-1-diffrejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffstale">0</div>
<div id="cbip-table-1-diffstale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rejected">0</div>
<div id="cbip-table-1-rejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-discarded">0</div>
<div id="cbip-table-1-discarded"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-stale">0</div>
<div id="cbip-table-1-stale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharedifficulty">0</div>
<div id="cbip-table-1-lastsharedifficulty"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharetime">Never</div>
<div id="cbip-table-1-lastsharetime"></div>
</td>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-pool">total</div>
<div id="cbip-table-1-pool"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-url"></div>
<div id="cbip-table-1-url"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-user"></div>
<div id="cbip-table-1-user"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status"></div>
<div id="cbip-table-1-status"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff"></div>
<div id="cbip-table-1-diff"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-getworks">28</div>
<div id="cbip-table-1-getworks"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-priority"></div>
<div id="cbip-table-1-priority"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-accepted">7</div>
<div id="cbip-table-1-accepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff1shares">0</div>
<div id="cbip-table-1-diff1shares"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffaccepted">458,752</div>
<div id="cbip-table-1-diffaccepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffrejected">0</div>
<div id="cbip-table-1-diffrejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffstale">0</div>
<div id="cbip-table-1-diffstale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rejected">0</div>
<div id="cbip-table-1-rejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-discarded">411</div>
<div id="cbip-table-1-discarded"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-stale">0</div>
<div id="cbip-table-1-stale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharedifficulty"></div>
<div id="cbip-table-1-lastsharedifficulty"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharetime"></div>
<div id="cbip-table-1-lastsharetime"></div>
</td>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-pool">HW</div>
<div id="cbip-table-1-pool"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-url">215</div>
<div id="cbip-table-1-url"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-user"></div>
<div id="cbip-table-1-user"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status"></div>
<div id="cbip-table-1-status"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff"></div>
<div id="cbip-table-1-diff"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-getworks"></div>
<div id="cbip-table-1-getworks"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-priority"></div>
<div id="cbip-table-1-priority"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-accepted"></div>
<div id="cbip-table-1-accepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diff1shares">0</div>
<div id="cbip-table-1-diff1shares"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffaccepted">0.0469%</div>
<div id="cbip-table-1-diffaccepted"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffrejected"></div>
<div id="cbip-table-1-diffrejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-diffstale"></div>
<div id="cbip-table-1-diffstale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rejected"></div>
<div id="cbip-table-1-rejected"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-discarded"></div>
<div id="cbip-table-1-discarded"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-stale"></div>
<div id="cbip-table-1-stale"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharedifficulty"></div>
<div id="cbip-table-1-lastsharedifficulty"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-lastsharetime"></div>
<div id="cbip-table-1-lastsharetime"></div>
</td>
</table>
</div>
</fieldset>
<!-- /tblsection -->
<!-- tblsection -->
<fieldset class="cbi-section" id="cbi-table-table">
<legend>AntMiner</legend>
<div class="cbi-section-descr"></div>
<div class="cbi-section-node">
<table id="ant_devs" class="cbi-section-table">
<tr class="cbi-section-table-titles">
<th class="cbi-section-table-cell">Chain#</th>
<th class="cbi-section-table-cell">ASIC#</th>
<th class="cbi-section-table-cell">Frequency(avg)</th>
<th class="cbi-section-table-cell">GH/S(ideal)</th>
                                <th class="cbi-section-table-cell">GH/S(RT)</th>
<th class="cbi-section-table-cell">HW</th>
<th class="cbi-section-table-cell">Temp(Chip1)</th>
                <th class="cbi-section-table-cell">Temp(Chip2)</th>
<th class="cbi-section-table-cell">ASIC status</th>
</tr>
<tr class="cbi-section-table-descr">
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
                                <th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
<th class="cbi-section-table-cell"></th>
</tr>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-chain">6</div>
<div id="cbip-table-1-chain"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-asic">63</div>
<div id="cbip-table-1-asic"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-frequency">670.63</div>
<div id="cbip-table-1-frequency"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rate2">4,718.25</div>
<div id="cbip-table-1-rate2"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rate">4,768.34</div>
<div id="cbip-table-1-rate"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-hw">1</div>
<div id="cbip-table-1-hw"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-temp">-</div>
<div id="cbip-table-1-temp"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-temp2">80</div>
<div id="cbip-table-1-temp2"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status"> oooooooo oooooooo oooooooo oooooooo oooooooo oooooooo oooooooo ooooooo</div>
<div id="cbip-table-1-status"></div>
</td>
</tr>
<tr class="cbi-section-table-row cbi-rowstyle-1" id="cbi-table-1">
<td class="cbi-value-field">
<div id="cbi-table-1-chain">Total</div>
<div id="cbip-table-1-chain"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-asic">63</div>
<div id="cbip-table-1-asic"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-frequency">670.63</div>
<div id="cbip-table-1-frequency"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rate2">13,000.00</div>
<div id="cbip-table-1-rate2"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-rate">4,768.34</div>
<div id="cbip-table-1-rate"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-hw"></div>
<div id="cbip-table-1-hw"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-temp"></div>
<div id="cbip-table-1-temp"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-temp2"></div>
<div id="cbip-table-1-temp2"></div>
</td>
<td class="cbi-value-field">
<div id="cbi-table-1-status"></div>
<div id="cbip-table-1-status"></div>
</td>
</tr>
</table>
</div>
<div class="cbi-section-node" style="margin-top:8px;">
<table id="ant_fans" class="cbi-section-table">
<tr class="cbi-section-table-titles">
<th class="cbi-section-table-cell" style="width:10%;">Fan#</th>
<th class="cbi-section-table-cell">Fan1</th>
<th class="cbi-section-table-cell">Fan2</th>
<th class="cbi-section-table-cell">Fan3</th>
<th class="cbi-section-table-cell">Fan4</th>
<th class="cbi-section-table-cell">Fan5</th>
                                                                <th class="cbi-section-table-cell">Fan6</th>
                                                                <th class="cbi-section-table-cell">Fan7</th>
                                                                <th class="cbi-section-table-cell">Fan8</th>
</tr>
<tr class="cbi-section-table-row">
<th class="cbi-rowstyle-1 cbi-value-field">Speed (r/min)</th>
</td>
<td id="ant_fan1" class="cbi-rowstyle-1 cbi-value-field">0</td>
<td id="ant_fan2" class="cbi-rowstyle-1 cbi-value-field">0</td>
<td id="ant_fan3" class="cbi-rowstyle-1 cbi-value-field">0</td>
<td id="ant_fan4" class="cbi-rowstyle-1 cbi-value-field">0</td>
<td id="ant_fan5" class="cbi-rowstyle-1 cbi-value-field">5,400</td>
<td id="ant_fan6" class="cbi-rowstyle-1 cbi-value-field">5,040</td>
<td id="ant_fan7" class="cbi-rowstyle-1 cbi-value-field">0</td>
<td id="ant_fan8" class="cbi-rowstyle-1 cbi-value-field">0</td>
</tr>
</table>
</div>
</fieldset>
<!-- /tblsection -->
<br />
</div>
<div class="clear"></div>
</div>
</div>
<div class="clear"></div>
<div style="text-align: center; bottom: 0; left: 0; height: 1.5em; font-size: 80%; margin: 0; padding: 5px 0px 2px 8px; background-color: #918ca0; width: 100%;">
<font style="color:#fff;">Copyright &copy; 2013-2014, Bitmain Technologies</font>
</div>
</body>
</html>
