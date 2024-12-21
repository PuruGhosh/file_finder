# file_finder

## Requirement:
+   python 3.x

## How to use:
```commandline
    python ./file_finder.py --path "<path>" --keyword "<keyword>"
```

## Example response:
```commandline
    $ python ./file_finder.py --path "path" --keyword "file"
    {'keyword': 'file', 'is_present': True, 'file_count': 3, 'files': ['2file.txt', 'file1.txt', 'file.log']}
```

