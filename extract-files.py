#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'system_ext/etc/permissions/moto-telephony.xml': blob_fixup()
        .regex_replace('/system/', '/system_ext/'),
    ('system_ext/etc/permissions/vendor.qti.hardware.data.connection-V1.0-java.xml', 'system_ext/etc/permissions/vendor.qti.hardware.data.connection-V1.1-java.xml'): blob_fixup()
        .regex_replace('/product/', '/system_ext/'),
    ('system_ext/lib/lib-imsvideocodec.so', 'system_ext/lib64/lib-imsvideocodec.so'): blob_fixup()
        .add_needed('libgui_shim.so'),
    'system_ext/priv-app/ims/ims.apk': blob_fixup()
        .apktool_patch('ims-patches'),
    'vendor/etc/permissions/com.motorola.androidx.camera.extensions.xml': blob_fixup()
        .regex_replace('system_ext', 'product'),
}  # fmt: skip

module = ExtractUtilsModule(
    'sm7250-common',
    'motorola',
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
