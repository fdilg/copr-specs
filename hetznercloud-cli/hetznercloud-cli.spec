Name:           hetznercloud-cli
Version:        1.65.0
Release:        1%{?dist}
Summary:        CLI for Hetzner Cloud

License:        MIT
URL:            https://github.com/hetznercloud/cli
Source0:        https://github.com/hetznercloud/cli/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang

%global debug_package %{nil}

%description
hetznercloud-cli is a command-line interface for managing Hetzner Cloud resources.

%prep
%autosetup -n cli-%{version}

%build
go build \
  -buildmode=pie \
  -trimpath \
  -o hcloud \
  ./cmd/hcloud

%install
install -Dpm 0755 hcloud %{buildroot}%{_bindir}/hcloud

%files
%license LICENSE
%doc README.md
%{_bindir}/hcloud

%changelog
* Sun Jun 14 2026 Frauke Dilg <frauke@dilg.dev> - 1.65.0-1
- Initial automated Copr packaging