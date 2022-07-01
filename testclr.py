from supports_color import supportsColor

if supportsColor.stdout:
    print('Terminal stdout supports color');

if supportsColor.stdout.has256:
    print('Terminal stdout supports 256 colors');

if supportsColor.stderr.has16m:
    print('Terminal stderr supports 16 million colors (truecolor)');