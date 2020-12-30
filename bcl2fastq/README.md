如果按lane拆分命令如下：

    dragen --bcl-conversion-only true --bcl-input-directory ${1} --output-directory ${2} --force --sample-sheet  ${3}

如果不按lane拆分命令下：

    dragen --bcl-conversion-only true --bcl-input-directory ${1} --output-directory ${2} --force --sample-sheet  ${3} --no-lane-splitting true