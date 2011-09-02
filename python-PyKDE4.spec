#
# Conditional build:
%define		_state		stable
%define		orgname		pykde4
%define		qtver		4.7.3
%define		sipver		2:4.12
%define		pyqtver		4.8.2-3

Summary:	PyKDE4 - Python bindings for KDE 4
Summary(pl.UTF-8):	PyKDE4 - dowiązania KDE 4 dla Pythona
Name:		python-PyKDE4
Version:	4.7.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	53fc1c1e1bacb1600a82c94352348fdd
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{version}
BuildRequires:	python-PyQt4-devel >= %{pyqtver}
BuildRequires:	python-sip >= %{sipver}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	python-PyQt4 >= %{pyqtver}
Requires:	python-sip >= %{sipver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyKDE4 is a set of Python bindings for the KDE 4 desktop environment.
The bindings are implemented as a set of Python modules, which
correspond to KDE libraries.

%description -l pl.UTF-8
PyKDE4 to zbiór dowiązań środowiska graficznego KDE 4 dla Pythona.
Dowiązania są zaimplementowane jako zbiór modułów Pythona
odpowiadających poszczególnym bibliotekom KDE.

%package devel
Summary:	SIP development files for PyKDE4
Summary(pl.UTF-8):	Pliki programistyczne SIP dla PyKDE4
Group:		Development/Languages/Python
Requires:	python-PyKDE4 = %{version}-%{release}
Requires:	python-PyQt4-devel >= %{pyqtver}
Requires:	python-sip-devel >= %{sipver}

%description devel
SIP development files for PyKDE4, needed to build other bindings for
C++ classes that inherit from any of the KDE4 classes.

%description devel -l pl.UTF-8
Pliki programistyczne SIP dla PyKDE4, potrzebne do budowania innych
dowiązań do klas C++ dziedziczących z dowolnej klasy KDE4.

%package devel-tools
Summary:	PyKDE4 development tools
Summary(pl.UTF-8):	Narzędzia programistyczne PyKDE4
Group:		Development/Languages/Python
Requires:	python-PyKDE4 = %{version}-%{release}
Requires:	python-PyQt4-devel-tools >= %{pyqtver}

%description devel-tools
PyKDE4 development tool: pykdeuic4.

%description devel-tools -l pl.UTF-8
Narzędzie programistyczne PyKDE4: pykdeuic4.

%package examples
Summary:	PyKDE4 examples
Summary(pl.UTF-8):	Przykłady dla PyKDE4
Group:		Libraries/Python

%description examples
PyKDE4 examples.

%description examples -l pl.UTF-8
Przykłady dla PyKDE4.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-PyKDE4-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_datadir}/apps/pykde4/examples/* $RPM_BUILD_ROOT%{_examplesdir}/python-PyKDE4-%{version}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4

# don't use py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/PyKDE4/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kpythonpluginfactory.so
%dir %{py_sitedir}/PyKDE4
%attr(755,root,root) %{py_sitedir}/PyKDE4/akonadi.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/dnssd.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kdecore.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kdeui.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/khtml.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kio.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/knewstuff.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kparts.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kterminal.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/ktexteditor.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/kutils.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/nepomuk.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/phonon.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/plasma.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/solid.so
%attr(755,root,root) %{py_sitedir}/PyKDE4/soprano.so
%{py_sitedir}/PyKDE4/__init__.py[co]
%{py_sitedir}/PyKDE4/pykdeconfig.py[co]

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/sip/PyKDE4
%{_datadir}/sip/PyKDE4/akonadi
%{_datadir}/sip/PyKDE4/dnssd
%{_datadir}/sip/PyKDE4/kdecore
%{_datadir}/sip/PyKDE4/kdeui
%{_datadir}/sip/PyKDE4/khtml
%{_datadir}/sip/PyKDE4/kio
%{_datadir}/sip/PyKDE4/knewstuff
%{_datadir}/sip/PyKDE4/kparts
%{_datadir}/sip/PyKDE4/kterminal
%{_datadir}/sip/PyKDE4/ktexteditor
%{_datadir}/sip/PyKDE4/kutils
%{_datadir}/sip/PyKDE4/nepomuk
%{_datadir}/sip/PyKDE4/phonon
%{_datadir}/sip/PyKDE4/plasma
%{_datadir}/sip/PyKDE4/polkitqt
%{_datadir}/sip/PyKDE4/solid
%{_datadir}/sip/PyKDE4/soprano
%{_datadir}/sip/PyKDE4/glossary.html

%files devel-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pykdeuic4
%{py_sitedir}/PyQt4/uic/pykdeuic4.py*
%{py_sitedir}/PyQt4/uic/widget-plugins/kde4.py*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python-PyKDE4-%{version}
