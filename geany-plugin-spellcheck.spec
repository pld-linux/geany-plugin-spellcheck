Summary:	geany spell check plugin
Summary(pl.UTF-8):	wtyczka dla geany sprawdzająca pisownię
Name:		geany-plugin-spellcheck
Version:	0.4
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://plugins.geany.org/spellcheck/spellcheck-%{version}.tar.bz2
# Source0-md5:	f03dca77cf65ea02c3fca9cff8cf4828
URL:		http://plugins.geany.org/spellcheck/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	enchant-devel
BuildRequires:	geany-devel >= 0.16
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.8
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires:	enchant
Requires:	enchant-backend
Requires:	geany >= 0.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This plugin checks the content of the current document in Geany with
the spell check library Enchant. You can also select a certain text
passage, then the plugin will only check the selected text.

%description -l pl.UTF-8
Ta wtyczka sprawdza treść bieżącego dokumentu w Geany, wykorzystując
bibliotekę do sprawdzania pisowni enchant. Możesz również wybrać
fragment tekstu, wtedy wtyczka sprawdzi jedynie zaznaczony tekst.

%prep
%setup -q -n spellcheck-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv  $RPM_BUILD_ROOT%{_docdir}/geany-plugins/spellcheck/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
rm -r $RPM_BUILD_ROOT%{_docdir}/geany-plugins

%find_lang geanyspellcheck

%clean
rm -rf $RPM_BUILD_ROOT

%files -f geanyspellcheck.lang
%defattr(644,root,root,755)
%{_libdir}/geany/*
%doc AUTHORS COPYING ChangeLog NEWS README
