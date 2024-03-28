# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate minspan

Name:           rust-minspan
Version:        0.1.1
Release:        %autorelease
Summary:        Package for determining the minimum span of one vector within another

License:        MIT
URL:            https://crates.io/crates/minspan
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A package for determining the minimum span of one vector within another.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
# FIXME: no license files detected
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
