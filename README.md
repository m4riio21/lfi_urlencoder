# lfi_urlencoder
Simple script to urlencode a LFI payload

```bash
python3 urlencoder.py <path_to_encode> [--double]
```

## Examples

Simple method, urlencodes every character to hex representation.

```bash
python3 urlencoder.py /etc/passwd
```

```cat
%2f%65%74%63%2f%70%61%73%73%77%64
```

Double urlencoding, evade advanced detection

```bash
python3 urlencoder.py /etc/passwd --double
```

```cat
%25%32%66%25%36%35%25%37%34%25%36%33%25%32%66%25%37%30%25%36%31%25%37%33%25%37%33%25%37%37%25%36%34
```
