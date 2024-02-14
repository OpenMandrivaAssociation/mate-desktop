#!/bin/sh
mate_pkg=mate-desktop

# mate curret version
v=`curl -s https://pub.mate-desktop.org/releases/ 2>/dev/null |sed -ne 's,.*href="\([[:digit:]].*\)\/".*,\1,p' |grep [0,2,4,6,8]$ |sort --sort=version |tail -n1`

curl -sL https://pub.mate-desktop.org/releases/$v 2>/dev/null |sed -ne "s,.*href=\"$mate_pkg-\(.*\)*.tar.xz\".*,\1,p" |sort --sort=version |tail -n1

