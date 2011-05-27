%define		_class		Search
%define		_subclass	Mnogosearch
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(config.php)

Name:		php-pear-%{upstream_name}
Version:	0.1.1
Release:	%mkrel 12
Summary:	Wrapper classes for the mnoGoSearch extention
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Search_Mnogosearch/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides wrapper classes for the mnoGoSearch search
engine. The package has two central classes "Search_Mnogosearch" and
"Search_Mnogosearch_Result". The class "Search_Mnogosearch" gives an
object that represents the search and the "Search_Mnogosearch_Result"
the result. The usage is just like the usage in the "DB" and
"DB_result" classes.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
