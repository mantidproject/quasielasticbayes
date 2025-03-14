./scripts/clean.sh

meson setup builddir -Dbuildtype=release

meson compile -C builddir
