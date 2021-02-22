# noinspection PyUnusedLocal
def main(device, *args, **kwargs):
    # Fresh browser launch with default browser check and first run check disabled
    device.shell('pm clear com.android.chrome')
    device.shell('am set-debug-app --persistent com.android.chrome')
    device.shell('echo "chrome --disable-fre --no-default-browser-check --no-first-run" > /data/local/tmp/chrome-command-line')
    
    # Enable permissions for Chrome
    device.shell('pm grant com.android.chrome android.permission.RECORD_AUDIO')
    device.shell('pm grant com.android.chrome android.permission.CAMERA')
    device.shell('pm grant com.android.chrome android.permission.WRITE_EXTERNAL_STORAGE')
    device.shell('pm grant com.android.chrome android.permission.READ_EXTERNAL_STORAGE')
