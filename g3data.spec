Summary:	g3data - utility for extracting data from graphs
Summary(pl.UTF-8):	g3data - narzędzie do wydobywania danych z wykresów
Name:		g3data
Version:	1.4.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.acclab.helsinki.fi/~frantz/software/%{name}-%{version}.tar.gz
# Source0-md5:	df4a134cba4981ad0d99536afeeeed4a
URL:		http://www.acclab.helsinki.fi/~frantz/software/g3data.php
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
g3data is used for extracting data from graphs. In publications graphs
often are included, but the actual data is missing. g3data makes the
extracting process much easier.

%description -l pl.UTF-8
g3data służy do wydobywania danych z wykresów. Często do publikacji
dołączane są wykresy, lecz brakuje aktualnych danych. g3data ułatwia
wydobycie tych danych z wykresów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="`pkg-config --cflags gtk+-2.0` %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
gzip -dc %{name}.1.gz >$RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TEST test*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
