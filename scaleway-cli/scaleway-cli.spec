Name:           scaleway-cli
Version:        2.56.3
Release:        1%{?dist}
Summary:        CLI for Scaleway Cloud

License:        Apache License 2.0
URL:            https://github.com/scaleway/scaleway-cli
Source0:        https://github.com/scaleway/scaleway-cli/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang >= 1.26.0

%global debug_package %{nil}

%description
scaleway-cli is a command-line interface for managing Scaleway Cloud resources.

%prep
%autosetup -n scaleway-cli-%{version}

%build
go build \
  -buildmode=pie \
  -trimpath \
  -o scw \
  ./cmd/scw

%install
install -Dpm 0755 scw %{buildroot}%{_bindir}/scw

%files
%license LICENSE
%doc README.md
%{_bindir}/scw

%changelog
* Sun Jun 14 2026 Frauke Dilg <frauke@dilg.dev> - 2.56.3-1
- Initial automated Copr packaging