rename.sh
=========

Simple script to rename ```.png``` and ```.jpg``` files in the current directory by index position (given by the iteration on the file system). In addition it is possible to specify a prefix that will be set before the index.

Usage : 
```bash
./rename.sh [prefix]
```

Example:

Assume we want to rename a bunch of JPG files in current dir listed here:
```bash
$ ls -1 
file_a.jpg
file_b.jpg
file_c.jpg
```

By default:
```bash
$ ./rename.sh
```

The files will be renamed as follows:

```bash
$ ls -1
1.jpg
2.jpg
3.jpg
```

When executing the script with prefix `my-prefix`:

```bash
$ ./rename.sh my-prefix
```

The files will be renamed as follows:

```bash
$ ls -1 
my-prefix-1.jpg
my-prefix-2.jpg
my-prefix-3.jpg
```
To ignore warnings with incompatible file types we simply add option -i :

```bash
$ ./rename.sh -i my-prefix
```

