Name: hunspell-uz
Summary: Uzbek hunspell dictionaries
Version: 0.6
Release: 3.1%{?dist}
Source0: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list/uzbek-wordlist-%{version}.tar.bz2
Group: Applications/Text
URL: http://www-user.uni-bremen.de/~kmashrab/uzbek-word-list
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Uzbek hunspell dictionaries.

%prep
%setup -q -n uzbek-wordlist-%{version}

%build
cd hunspell
make
cp -p README ../README.hunspell

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hunspell/uz_UZ* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog Copyright README README.hunspell COPYING TODO
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.6-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 20 2006 Caolan McNamara <caolanm@redhat.com> - 0.6-1
- initial version
