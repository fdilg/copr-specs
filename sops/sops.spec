Name:           sops
Version:        3.13.1
Release:        1%{?dist}
Summary:        SOPS is an editor of encrypted files

License:        Mozilla Public License 2.0
URL:            https://github.com/getsops/sops
Source0:        https://github.com/getsops/sops/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang

%global debug_package %{nil}

%description
SOPS is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats and encrypts with AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, and PGP.

%prep
%autosetup -n sops-%{version}

%build
go build \
  -buildmode=pie \
  -trimpath \
  -o sops \
  ./cmd/sops

%install
install -Dpm 0755 sops %{buildroot}%{_bindir}/sops

%files
%license LICENSE
%doc README.rst
%{_bindir}/sops

%changelog
* Sun Jun 14 2026 Frauke Dilg <frauke@dilg.dev> - 1.65.0-1
- Initial automated Copr packaging