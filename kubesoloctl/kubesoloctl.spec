Name:           kubesoloctl
Version:        1.2.3
Release:        1%{?dist}
Summary:        A single binary that manages the whole KubeSolo lifecycle

License:        MIT
URL:            https://github.com/portainer/kubesolo
Source0:        https://github.com/portainer/kubesolo/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang

%global debug_package %{nil}

%description
kubesoloctl  is a single, dependency-free binary that manages the whole KubeSolo lifecycle: pre-flight checks, download, service setup, kubeconfig wiring, configuration, upgrades, reset and uninstall.

%prep
%autosetup -n kubesolo-%{version}

%build
go build \
  -buildmode=pie \
  -trimpath \
  -o kubesoloctl \
  ./cmd/kubesoloctl

%install
install -Dpm 0755 kubesoloctl %{buildroot}%{_bindir}/kubesoloctl

%files
%license LICENSE
%doc README.md
%{_bindir}/kubesoloctl

%changelog
* Sun Nov 08 2026 Frauke Dilg <frauke@dilg.dev> - 1.2.3-1
- Update to latest version
* Sun Oct 25 2026 Frauke Dilg <frauke@dilg.dev> - 1.2.2-1
- Initial automated Copr packaging
