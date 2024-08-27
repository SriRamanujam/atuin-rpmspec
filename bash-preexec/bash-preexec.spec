Name:           bash-preexec
Version:        0.5.0
Release:        %autorelease
Summary:        preexec and precmd functions for Bash just like Zsh

License:        MIT
URL:            https://github.com/rcaloras/bash-preexec
Source:         https://github.com/rcaloras/bash-preexec/archive/refs/tags/%{version}.tar.gz

# Fix tests
Patch:          https://github.com/rcaloras/bash-preexec/commit/a44754f5c3ca76b0330324680670cb8574d2768f.patch

BuildRequires:  bats
BuildArch: noarch

%description
preexec and precmd hook functions for Bash 3.1+ in the style of Zsh. They aim to
emulate the behavior as described for Zsh.


%prep
%autosetup -p1


%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -Dpm 644 bash-preexec.sh %{buildroot}%{_sysconfdir}/profile.d/bash-preexec.sh


%check
bats test

%files
%license LICENSE.md
%doc README.md
%{_sysconfdir}/profile.d/bash-preexec.sh


%changelog
%autochangelog

