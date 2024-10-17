%define name evolution-remove-duplicates
%define version 0.0.4
%define oname remove-duplicates-plugin
%define release %mkrel 4

Summary: Plugin for Evolution that removed duplicated emails
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{oname}-%{version}.tar.gz
License: GPLv2
Group: Networking/Mail
Url: https://www.gnome.org/~carlosg/stuff/evolution/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evolution-devel
Requires: evolution

%description
This is a plugin for evolution for deleting duplicated mails without
big headaches.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%_libdir/evolution/*/plugins/liborg-gnome-remove-duplicates.la
%_libdir/evolution/*/plugins/liborg-gnome-remove-duplicates.so
%_libdir/evolution/*/plugins/org-gnome-remove-duplicates.eplug
%_libdir/evolution/*/plugins/org-gnome-remove-duplicates.xml
%_datadir/evolution/*/errors/org-gnome-remove-duplicates.error

