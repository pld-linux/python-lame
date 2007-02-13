Summary:	Python bindings for libmp3lame
Summary(pl.UTF-8):	Dowiązania Pythona dla libmp3lame
Name:		python-lame
Version:	0.1
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/lame/py-lame-%{version}.tar.gz
# Source0-md5:	40c1cdab4359fd36d356159327b53cfb
URL:		http://lame.sourceforge.net/
BuildRequires:	lame-libs-devel
BuildRequires:	python-devel
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libmp3lame.

%description -l pl.UTF-8
Dowiązania Pythona dla libmp3lame.

%prep
%setup -q -n py-lame-%{version}

%build
%{__make} -f Makefile.pre.in boot
%{__make} \
	OPT="%{rpmcflags} %{!?debug:-DNDEBUG} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_libdir}

%{__make} install \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc API README
%attr(755,root,root) %{py_sitedir}/*.so
