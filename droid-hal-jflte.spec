# These and other macros are documented in dhd/droid-hal-device.inc

%define device jflte
%define vendor samsung
%define vendor_pretty Samsung
%define device_pretty Galaxy S4 intl LTE

%define installable_zip 1

# Entries migrated from the old rpm/droid-hal-jflte.spec
%define android_config \
#define QCOM_BSP 1\
%{nil}

%include rpm/dhd/droid-hal-device.inc
