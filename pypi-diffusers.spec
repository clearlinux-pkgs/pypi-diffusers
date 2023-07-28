#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-diffusers
Version  : 0.19.1
Release  : 16
URL      : https://files.pythonhosted.org/packages/f5/93/f9247752a5a171ff74e3424bc589b6f6b350511c509fae6456b83ee2eb9f/diffusers-0.19.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/93/f9247752a5a171ff74e3424bc589b6f6b350511c509fae6456b83ee2eb9f/diffusers-0.19.1.tar.gz
Summary  : Diffusers
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-diffusers-bin = %{version}-%{release}
Requires: pypi-diffusers-license = %{version}-%{release}
Requires: pypi-diffusers-python = %{version}-%{release}
Requires: pypi-diffusers-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<br>
<img src="https://github.com/huggingface/diffusers/blob/main/docs/source/en/imgs/diffusers_library.jpg" width="400"/>
<br>
<p>
<p align="center">
<a href="https://github.com/huggingface/diffusers/blob/main/LICENSE">
<img alt="GitHub" src="https://img.shields.io/github/license/huggingface/datasets.svg?color=blue">
</a>
<a href="https://github.com/huggingface/diffusers/releases">
<img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/diffusers.svg">
</a>
<a href="CODE_OF_CONDUCT.md">
<img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg">
</a>
</p>

%package bin
Summary: bin components for the pypi-diffusers package.
Group: Binaries
Requires: pypi-diffusers-license = %{version}-%{release}

%description bin
bin components for the pypi-diffusers package.


%package license
Summary: license components for the pypi-diffusers package.
Group: Default

%description license
license components for the pypi-diffusers package.


%package python
Summary: python components for the pypi-diffusers package.
Group: Default
Requires: pypi-diffusers-python3 = %{version}-%{release}

%description python
python components for the pypi-diffusers package.


%package python3
Summary: python3 components for the pypi-diffusers package.
Group: Default
Requires: python3-core
Provides: pypi(diffusers)
Requires: pypi(filelock)
Requires: pypi(huggingface_hub)
Requires: pypi(importlib_metadata)
Requires: pypi(numpy)
Requires: pypi(pillow)
Requires: pypi(regex)
Requires: pypi(requests)
Requires: pypi(safetensors)

%description python3
python3 components for the pypi-diffusers package.


%prep
%setup -q -n diffusers-0.19.1
cd %{_builddir}/diffusers-0.19.1
pushd ..
cp -a diffusers-0.19.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690554780
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-diffusers
cp %{_builddir}/diffusers-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-diffusers/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/diffusers-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-diffusers/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
