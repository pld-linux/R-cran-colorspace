%define		fversion	%(echo %{version} |tr r -)
%define		modulename	colorspace
Summary:	Color Space Manipulation
Name:		R-cran-%{modulename}
Version:	1.2r4
Release:	2
License:	BSD
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	1f9a05587ffae27fc3e4da7503d016fc
URL:		http://cran.fhcrc.org/web/packages/colorspace/index.html
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Carries out mapping between assorted color spaces including RGB, HSV,
HLS, CIEXYZ, CIELUV, HCL (polar CIELUV), CIELAB and polar CIELAB.
Qualitative, sequential, and diverging color palettes based on HCL
colors are provided.

%prep
%setup -q -c

%build
R CMD build %{modulename} --no-build-vignettes

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
