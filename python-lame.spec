%include	/usr/lib/rpm/macros.python
Summary:	Python bindings for libmp3lame
Summary(pl):	Dowiązania Pythona dla libmp3lame
Name:		python-lame
Version:	0.1
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/lame/py-lame-%{version}.tar.gz
URL:		http://lame.sourceforge.net/
BuildRequires:	lame-libs-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libmp3lame.

%description -l pl
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
