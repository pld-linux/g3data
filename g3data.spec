Summary:	g3data is used for extracting data from graphs
Summary(pl):	g3data s³u¿y do wydobywania danych z wykresów
Name:		g3data
Version:	1.4.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.acclab.helsinki.fi/~frantz/software/%{name}-%{version}.tar.gz
# Source0-md5:	5732f05bae15c0e1df7423be58c800cb
URL:		http://www.acclab.helsinki.fi/~frantz/software/g3data.php
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
g3data is used for extracting data from graphs. In publications graphs
often are included, but the actual data is missing. g3data makes the
extracting process much easier.

%description -l pl
g3data s³u¿y do wydobywania danych z wykresów. Czêsto do publikacji
do³±czane s± wykresy, lecz brakuje aktualnych danych. g3data u³atwia
wydobycie tych danych z wykresów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="`pkg-config --cflags gtk+-2.0` %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TEST test*
%attr(755,root,root) %{_bindir}/*
