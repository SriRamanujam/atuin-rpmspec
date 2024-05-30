# Generated by rust2rpm 26
%bcond_without check

Name:           atuin
Version:        18.3.0
Release:        %autorelease
Summary:        magical shell history

%global _license %{shrink:
((Apache-2.0 OR MIT) AND BSD-3-Clause) AND
((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND
(0BSD OR MIT OR Apache-2.0) AND
(Apache-2.0) AND
(Apache-2.0 AND MIT) AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 OR BSL-1.0 OR MIT) AND
(Apache-2.0 OR ISC OR MIT) AND
(Apache-2.0 OR MIT) AND
(Apache-2.0 OR MIT OR Zlib) AND
(Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
(BSD-2-Clause OR Apache-2.0 OR MIT) AND
(BSD-3-Clause) AND
(BSD-3-Clause AND MIT) AND
(ISC) AND
(ISC AND MIT AND OpenSSL) AND
(MIT) AND
(MPL-2.0) AND
(Unlicense OR MIT)
}

License:       %_license

URL:            https://atuin.sh
Source:         https://github.com/atuinsh/atuin/archive/refs/tags/v%{version}.tar.gz
# * Fix dependencies
# * - Switch cli-clipboard for arboard
# *   https://github.com/atuinsh/atuin/pull/2067
# * - Bump metrics dependencies
# *   https://github.com/atuinsh/atuin/pull/2062
# * Cherry-picked in: https://github.com/LecrisUT/atuin/tree/fedora-18.3.0-patch
Patch10:       atuin-18.3.0-Fix_dependencies.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  protobuf-devel
%if %{with check}
BuildRequires:  postgresql-test-rpm-macros
%endif
Requires:       bash-preexec

%global _description %{expand:
Atuin replaces your existing shell history with a SQLite database, and records
additional context for your commands. Additionally, it provides optional and fully
encrypted synchronisation of your history between machines, via an Atuin server.
}

%description %{_description}

%prep
%autosetup -n atuin-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/atuin -t %{buildroot}%{_bindir}/
# Generate all of the shell-completions
for completion in bash fish zsh; do
  %{buildroot}%{_bindir}/atuin gen-completions --shell $completion -o .
done
install -Dpm 644 atuin.bash %{buildroot}%{_datadir}/bash-completion/completions/atuin
install -Dpm 644 atuin.fish %{buildroot}%{_datadir}/fish/completions/atuin
install -Dpm 644 _atuin %{buildroot}%{_datadir}/zsh/site-functions/atuin

# Add atuin to default profile
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/atuin.sh <<EOF
$(%{buildroot}%{_bindir}/atuin init bash)
EOF

%if %{with check}
%check
# start a postgres instance for the tests to use
export PGTESTS_LOCALE="C.UTF-8"
export PGTESTS_USERS="atuin:pass"
export PGTESTS_DATABASES="atuin:atuin"
export PGTESTS_PORT=5432
%postgresql_tests_run
%cargo_test
%endif

%files
%license LICENSE
%license crates/atuin/LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc CONTRIBUTORS
%doc README.md
%{_bindir}/atuin
%{_datadir}/bash-completion/completions/atuin
%{_datadir}/fish/completions/atuin
%{_datadir}/zsh/site-functions/atuin
%config %{_sysconfdir}/profile.d/atuin.sh

%changelog
%autochangelog
