# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-chat-activity
Version: 81
Release: 1
Summary: Instant messaging client for Sugar
License: GPLv2+
Group: Graphical desktop/Other
Url: https://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Chat/Chat-%{version}.tar.bz2

Requires: python2-simplejson  
Requires: sugar-toolkit-gtk3 >= 0.85.8

BuildRequires: gettext  
BuildRequires: sugar-toolkit-gtk3 >= 0.85.8

BuildArch: noarch

%description
The Chat activity will provide a simple interface for collaborative discussion,
be it between two individuals or among a group as large as an entire classroom.
While a lightweight and 'impermanent' chat will be provided in a layer above
all activities and the various mesh levels, this activity devoted to textual
communication will keep detailed records of the conversation within the journal
and provide a means of searching through the conversation to locate
important comments.

%prep
%setup -q -n Chat-%{version}


%build

rm -f MANIFEST
python2 setup.py build

%install
python2 setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
%find_lang org.laptop.Chat

%files -f org.laptop.Chat.lang
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING NEWS



%changelog
* Sat Sep 19 2009 Aleksey Lim <alsroot@mandriva.org> 66-1mdv2010.0
+ Revision: 444540
- Update to 66

* Mon Apr 06 2009 Aleksey Lim <alsroot@mandriva.org> 65-1mdv2009.1
+ Revision: 364287
- Sucrose 0.84.2 release

* Wed Mar 04 2009 Aleksey Lim <alsroot@mandriva.org> 64-1mdv2009.1
+ Revision: 348316
- Sucrose 0.84.0 release

* Mon Feb 23 2009 Aleksey Lim <alsroot@mandriva.org> 63-1mdv2009.1
+ Revision: 344204
- Sucrose 0.83.6 release

* Tue Jan 20 2009 Aleksey Lim <alsroot@mandriva.org> 62-1mdv2009.1
+ Revision: 331984
- new Sucrose 0.83.4 release

* Sun Jan 11 2009 Aleksey Lim <alsroot@mandriva.org> 61-1mdv2009.1
+ Revision: 328396
- initial commit

