Name: atuin
Version: 17.1.0
Release: %autorelease
Summary: Magical shell history

License: MIT
URL: https://github.com/atuinsh/atuin
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo
BuildRequires: rust
BuildRequires: gcc

%description
Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronisation of your history between machines, via an Atuin server.

%prep
%autosetup -p1


%install
cargo install --root=%{buildroot}%{_prefix} --path=.

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json

strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE
%doc README.md
%doc docs/docs
%{_bindir}/atuin


%changelog
%autochangelog

